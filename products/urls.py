from django.urls import path
from products.views import ProductListView, ProductBestsellerView, ProductReadmePickView, ProductRecommendView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/bestseller', ProductBestsellerView.as_view()),
    path('/recommend', ProductRecommendView.as_view()),
    path('/readmepick', ProductReadmePickView.as_view())
]
