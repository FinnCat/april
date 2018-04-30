from django.urls import path

from .views import home, create_product, detail_product, vote_product

urlpatterns = [
    path('', home, name='home_home'),
    path('create/', create_product, name='product_create'),
    path('<int:product_id>', detail_product, name='product_detail'),
    path('<int:product_id>/vote_product', vote_product, name='upvote'),
]