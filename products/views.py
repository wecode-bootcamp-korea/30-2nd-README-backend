import random

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Avg, Q, Count

from products.models  import Product, Series

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

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.count(),
            'product_id'    : book.id
        } for book in high_rating_books]    

        return JsonResponse({'result':result}, status=200)


class ProductRecommendView(View):
    def get(self, request):
        recommend_books = Product.objects.annotate(rating_avg=Avg('review__rating'), comment_count=Count('review__content')).\
                          order_by('-rating_avg', '-comment_count')

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.count(),
            'product_id'    : book.id
        } for book in recommend_books]

        return JsonResponse({'result':result}, status=200)


class ProductReadmePickView(View):
    def get(self, request):

        readme_pick_books = Product.objects.order_by('?')

        result = [{
            'name'          : book.name,
            'book_img'      : [book_img.image_url for book_img in book.image_set.all()],
            'author'        : book.author.name,
            'rating_avg'    : book.review_set.all().aggregate(Avg('rating'))['rating__avg'],
            'comment_count' : book.review_set.all().count(),
            'product_id'    : book.id
        } for book in readme_pick_books]

        return JsonResponse({'result':result}, status=200)       
