from django.urls import path
from webapp.views import (
    ProductView,
    ProductDetailView,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDelete,
)


urlpatterns = [
    path('', ProductView.as_view(), name='index_all'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:id>/update', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:id>/delete', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:id>/review/add/', ReviewCreateView.as_view(), name='review_add'),
    path('review/<int:id>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:id>/delete/', ReviewDelete.as_view(), name='review_delete'),
]