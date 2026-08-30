from pyexpat import model
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,ProductImage,Brand,Review

class Pr_Image_Inline(admin.TabularInline):
    model = ProductImage

class ProductImageAdmin(SummernoteModelAdmin):
    list_display =['name','price','flag']
    search_fields =['name','subtitle','descriptions']
    list_filter =['price','flag']

    inlines = [Pr_Image_Inline,]

    

    summernote_fields =('subtitle','descriptions')
    


admin.site.register(Product,ProductImageAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Review)
