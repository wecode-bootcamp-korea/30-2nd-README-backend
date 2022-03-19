from django.urls import path

from .views import ReviewView, LikeView

urlpatterns = [
    path('/<int:product_id>', ReviewView.as_view()),
    path('/likes/<int:review_id>', LikeView.as_view())
]