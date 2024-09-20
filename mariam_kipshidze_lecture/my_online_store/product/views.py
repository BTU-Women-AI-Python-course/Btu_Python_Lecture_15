from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from product.forms import ProductForm, ProductUpdateForm
from product.models import Product

def product_list(request):
    objects = Product.objects.all()
    return render(request, 'product_list.html', {'objects': objects})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'object': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, 'product_update_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'The object was deleted successfully.')
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'object': product})
