from django.contrib import admin
from .models import ProductType, Product, Transaction

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
	model = ProductType

	list_display = ('name', 'description')
	search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	model = Product

	list_display = ('name', 'product_type', 'owner', 'description', 'price', 'stock', 'status')
	list_filter = ('product_type', 'owner', 'status')
	search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	model = Transaction

	list_display = ('buyer', 'product', 'amount', 'status', 'created_on')
	list_filter = ('buyer', 'product', 'status')
	date_hierarchy = 'created_on'
