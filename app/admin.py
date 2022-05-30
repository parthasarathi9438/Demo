from django.contrib import admin
from app.models import ProductModel

# Register your models here.
# admin.site.register(ProductModel)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']