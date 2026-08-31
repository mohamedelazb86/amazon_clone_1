from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('brands',views.brand_list,name='brand_list'),
    path('brands/<slug:slug>',views.brand_detail,name='brand_detail'),
    path('',views.product_list,name='product_list'),
    path('<slug:slug>',views.product_detail,name='product_detail'),
]
