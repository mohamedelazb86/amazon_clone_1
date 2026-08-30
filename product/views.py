from django.shortcuts import render

from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products=Product.objects.all().order_by('-id')[:20]
    context={
        'products':products
    }

    return render(request,'product/product_list.html',context)

@login_required
def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    context={
        'product':product
    }
    return render(request,'product/product_detail.html',context)
