import json

from django.http  import JsonResponse
from django.views import View

from users.models         import User
from reviews.models       import Review
from users.decorators     import login_decorator

class ReviewView(View):
    @login_decorator
    def get (self, request, product_id):
        try:
            user       = request.user 
            limit      = int(request.GET.get('limit', 10))
            offset     = int(request.GET.get('offset', 0))
            review_all = Review.objects.filter(product_id=product_id)
            my_review  = Review.objects.get(product_id=product_id, user_id=user.id)
            reviews    = review_all.exclude(user_id=user.id)[offset:offset+limit]
            
            top_review ={
                'review_id'  : my_review.id,
                'user_id'    : my_review.user_id,
                'nickname'   : User.objects.get(id=user.id).nickname,
                'rating'     : my_review.rating,
                'content'    : my_review.content,
                'created_at' : my_review.created_at.date(),
                'updated_at' : my_review.updated_at.date()
            }
            
            list_reviews = [{
                'review_id'  : review.id,
                'user_id'    : review.user_id,
                'nickname'   : User.objects.get(id=review.user_id).nickname,
                'rating'     : review.rating,
                'content'    : review.content,
                'created_at' : review.created_at.date(),
                'updated_at' : review.updated_at.date()
            } for review in reviews]
            
            results = {
                'top_review'  : top_review,
                'list_review' : list_reviews
            }
            return JsonResponse({'results':results}, status=200) 
        except Review.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_REVIEW'}, status=404)

    @login_decorator
    def post(self, request, product_id):
        try:
            data       = json.loads(request.body)
            user       = request.user
            rating     = data['rating']
            content    = data['content']
            
            if Review.objects.filter(user_id=user.id, product_id=product_id).exists():
                return JsonResponse({'message':'REVIEW_ALREADY_EXISTED'}, status=400)
            
            Review.objects.create(
                user_id    = user.id,
                product_id = product_id,
                rating     = rating,
                content    = content
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

    @login_decorator
    def patch(self, request, product_id):
        try:
            data      = json.loads(request.body)
            rating    = data['rating']
            content   = data['content']
            review_id = data['review_id']
            review    = Review.objects.get(id=review_id, product_id=product_id)
            
            review.rating  = rating
            review.content = content
            review.save()
            
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except Review.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_REVIEW'}, status=404)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

    @login_decorator
    def delete(self, request, product_id):
        try:
            user       = request.user
            review_id  = request.GET.get('review_id', None)
            reviews    = Review.objects.get(id=review_id, user_id=user.id, product_id=product_id)
            
            reviews.delete()
            
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except Review.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_REVIEW'}, status=404)