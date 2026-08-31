from django.shortcuts import render,get_object_or_404
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
    # product=Product.objects.get(slug=slug)
    product=get_object_or_404(Product,slug=slug)
    # images=ProductImage.objects.filter(product=product)
    images=product.images_product.all()
    # reviews=Review.objects.filter(product=product)
    reviews=product.review_product.all()
    related=Product.objects.filter(brand=product.brand)[:10]

    # المنتج السابق
   

    product_previous= Product.objects.filter(id__lt=product.id).order_by('-id').first()

    product_next=Product.objects.filter(id__gt=product.id).order_by('id').first()

    context={
        'product':product,
        'images':images,
        'reviews':reviews,
        'related':related,
        'product_previous':product_previous,
        'product_next':product_next,

    }
    return render(request,'product/product_detail.html',context)
