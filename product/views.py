from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product,ProductImage,Review
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products=Product.objects.all()
    paginator = Paginator(products, 20)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
  

    context={
        'products':products
    }

    return render(request,'product/product_list.html',context)

@login_required
def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    images=ProductImage.objects.filter(product=product)
    reviews=Review.objects.filter(product=product)
    related=Product.objects.filter(brand=product.brand)[:10]

    context={
        'product':product,
        'images':images,
        'reviews':reviews,
        'related':related
    }
    return render(request,'product/product_detail.html',context)
