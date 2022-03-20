import json

from django.http      import HttpResponse, JsonResponse
from django.views     import View
from django.db        import transaction

from users.decorators import login_decorator
from .models          import Cart,CartSeries
from products.models  import Series, Image


class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user

            data = json.loads(request.body)

            product_id = data['product_id']
            series_ids = data['series_ids']

            if self.series_does_not_exist(product_id, series_ids):
                return JsonResponse({'message' : 'SERIES_DOES_NOT_EXIEST'}, status = 404)

            with transaction.atomic():
                cart, cart_series = self.create_cart_and_cartseries(user, product_id, series_ids)

                CartSeries.objects.filter(cart_id = cart.id, series_id__in = series_ids).delete()
                CartSeries.objects.bulk_create(cart_series)

            return JsonResponse({'message' : 'CREATE_CART'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        

    @login_decorator
    def get(self, request):
        try:
            user = request.user
            
            carts_series = CartSeries.objects.select_related('cart', 'series').filter(cart__user = user)

            cart_list = [
                {
                'product_id'   : cart_series.cart.product.id,
                'series_id'    : cart_series.series.id,
                'author'       : cart_series.cart.product.author.name,
                'series_name'  : cart_series.series.name,
                'series_price' : cart_series.series.price,
                'image'        : Image.objects.get(product_id = cart_series.cart.product.id).image_url
                }
                for cart_series in carts_series
            ]

            return JsonResponse({'result' : cart_list}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except Image.DoesNotExist:
            return JsonResponse({'message' : 'IMAGE_DOES_NOT_EXIST'}, status = 404)

            
    @login_decorator
    def delete(self, request):
        try:
            user = request.user

            data = json.loads(request.body)

            cart_series = data['cart_series_id']

            carts = CartSeries.objects.filter(cart__user = user, id__in = cart_series)
            
            if not carts.exists():
                return JsonResponse({'message' : 'CART_DOES_NOT_EXIST'}, status = 404)

            carts.delete()

            return HttpResponse(status = 204)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    def series_does_not_exist(self, product_id, series_ids):
        for series in series_ids:
            if not Series.objects.filter(id = series, product_id = product_id).exists():
                return True
    
    def create_cart_and_cartseries(self, user, product_id, series_ids):
        cart,is_created = Cart.objects.get_or_create(
            user_id = user.id,
            product_id = product_id,
        )

        cart_series = [CartSeries(
                    cart_id   = cart.id,
                    series_id = series
                    ) for series in series_ids if Series.objects.filter(id = series, product_id = product_id)]
        
        return cart, cart_series
        