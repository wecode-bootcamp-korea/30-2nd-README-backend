import json, uuid

from django.http  import JsonResponse, HttpResponse
from django.views import View
from django.db    import transaction

from users.decorators import login_decorator
from .models          import Order, OrderSeries
from carts.models     import Cart, CartSeries

class OrderView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user

            data = json.loads(request.body)

            product_id = data['product_id']
            series_ids = data['series_ids']

            cart_series  = CartSeries.objects.select_related('cart', 'series')\
                                             .filter(cart__product_id = product_id, series_id__in = series_ids)
                                             
            with transaction.atomic():
                if not cart_series.exists():
                    return JsonResponse({'message' : 'CART_DOES_NOT_EXIST'}, status = 404)

                self.create_order_and_orderseries(user, product_id, series_ids)

                cart_series.delete() 

                self.delete_cartseries(product_id)
                
            return HttpResponse(status = 201)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
            
    def create_order_and_orderseries(self, user, product_id, series_ids):
        order, is_created = Order.objects.get_or_create(
            user_id      = user.id,
            product_id   = product_id,
            defaults     = {
                'order_number' : uuid.uuid4(),
            }
        )

        order_series = [
            OrderSeries(
            order_id  = order.id,
            series_id = series
            )
            for series in series_ids if CartSeries.objects.filter(series_id = series).exists()
        ]

        OrderSeries.objects.bulk_create(order_series)

    def delete_cartseries(self, product_id):
        if not CartSeries.objects.filter(cart__product_id = product_id):
            Cart.objects.filter(product_id = product_id).delete()