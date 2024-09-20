from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'objects'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'object'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['title', 'description', 'price']
    success_url = '/product/class_product_list/'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update_form.html'
    fields = ['title', 'description']
    success_url = '/product/class_product_list/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = '/product/success-url/'


class SuccessView(TemplateView):
    template_name = 'success.html'
