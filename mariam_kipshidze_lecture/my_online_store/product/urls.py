from django.urls import path

from product.class_views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, SuccessView
from product.views import product_list, product_detail, product_create, product_update, product_delete

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('product_create/', product_create, name='product_create'),
    path('product_update/<int:pk>', product_update, name='product_update'),
    path('product_delete/<int:pk>', product_delete, name='product_delete'),
    path('class_product_list/', ProductListView.as_view(), name='class_product_list'),
    path('class_product_detail/<int:pk>', ProductDetailView.as_view(), name='class_product_detail'),
    path('class_product_create/', ProductCreateView.as_view(), name='class_product_create'),
    path('class_product_update/<int:pk>', ProductUpdateView.as_view(), name='class_product_update'),
    path('class_product_delete/<int:pk>', ProductDeleteView.as_view(), name='class_product_delete'),
    path('success-url/', SuccessView.as_view(), name='success-url'),
]
