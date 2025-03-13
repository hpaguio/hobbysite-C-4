from django.contrib import admin
from .models import ProductType, Product

# Register your models here.

class ProductTypeAdmin(admin.ModelAdmin):
	model = ProductTypeAdmin

	list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
	model = Product

	list_display = ('name', 'product_type', 'description', 'price')

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
