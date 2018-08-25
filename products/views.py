from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Product, Category

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render (request, 'products/product_list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug ,available = True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render (request, 'products/product_detail.html', context)