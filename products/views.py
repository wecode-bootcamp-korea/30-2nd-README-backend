from django.views     import View
from django.http      import JsonResponse
from django.db.models import Avg, Q, Count

from products.models  import Product, Series, Image


class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category', None)
        offset   = int(request.GET.get('offset', 0))
        limit    = int(request.GET.get('limit', 9)) 

        books = Product.objects.order_by('?')

        if category:
            q = Q(category__name=category)
            books = Product.objects.filter(q)

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.count(),
            'product_id'    : book.id
        } for book in books[offset:offset+limit]]

        return JsonResponse({'result':result}, status=200)


class ProductBestsellerView(View):
    def get(self, request):
        high_rating_books = Product.objects.annotate(rating_avg=Avg('review__rating')).order_by('-rating_avg')
        offset            = int(request.GET.get('offset', 0))
        limit             = int(request.GET.get('limit', 6))

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.count(),
            'product_id'    : book.id
        } for book in high_rating_books[offset:offset+limit]]    

        return JsonResponse({'result':result}, status=200)


class ProductRecommendView(View):
    def get(self, request):
        recommend_books = Product.objects.annotate(rating_avg=Avg('review__rating'), comment_count=Count('review__content')).\
                          order_by('-rating_avg', '-comment_count')
        offset          = int(request.GET.get('offset', 0))
        limit           = int(request.GET.get('limit', 6))

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.count(),
            'product_id'    : book.id
        } for book in recommend_books[offset:offset+limit]]

        return JsonResponse({'result':result}, status=200)


class ProductReadmePickView(View):
    def get(self, request):
        readme_pick_books = Product.objects.order_by('?')
        offset            = int(request.GET.get('offset', 0))
        limit             = int(request.GET.get('limit', 6))

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.all().aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.all().count(),
            'product_id'    : book.id
        } for book in readme_pick_books[offset:offset+limit]]

        return JsonResponse({'result':result}, status=200)       


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            book         = Product.objects.get(id=product_id)
            book_img     = Image.objects.get(product_id=product_id)
            series_books = Series.objects.filter(product_id=product_id)

            total_price  = 0

            for series_book in series_books:
                total_price += series_book.price

            result = {
                'book_name'   : book.name,
                'author'      : book.author.name,
                'publisher'   : book.publisher.name,
                'book_img'    : book_img.image_url,
                'total_price' : total_price
            }
        except Product.DoesNotExist:
            return JsonResponse({'message':'product does not exist'}, status=400)

        return JsonResponse({'result':result}, status=200)

class SeriesListView(View):
    def get(self, request, product_id):
        series = Series.objects.filter(product_id=product_id)
        offset = int(request.GET.get("offset", 0))
        limit  = int(request.GET.get("limit", 10))

        result = [{
            'series_name'  : book.name,
            'series_image' : [image.image_url for image in book.product.image_set.filter(product_id=product_id)],
            'published_at' : book.published_at,
            'price'        : book.price,
            'series_id'    : book.id
        } for book in series[offset:offset+limit]]

        return JsonResponse({'result':result}, status=200)
        
