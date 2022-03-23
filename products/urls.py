from django.urls import path
from products.views import ProductListView, ProductBestsellerView, ProductReadmePickView, ProductRecommendView, ProductDetailView, SeriesListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/bestseller', ProductBestsellerView.as_view()),
    path('/recommend', ProductRecommendView.as_view()),
    path('/readmepick', ProductReadmePickView.as_view()),
    path('/details/<int:product_id>', ProductDetailView.as_view()),
    path('/books/<int:product_id>', SeriesListView.as_view())
]
