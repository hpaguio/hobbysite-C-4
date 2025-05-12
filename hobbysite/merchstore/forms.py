from django import forms
from .models import Product, Transaction

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		def get_product_type_names():
			names = dict()
			for type in Product.objects.values_list('product_type', flat=true).distinct():
				names[type] = type.name 
			return names
		fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'product_type': forms.Select(choices=get_product_type_names, attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'stock': forms.NumberInput(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'})
		}

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['amount']
		widgets = {
			'amount': forms.NumberInput(attrs={'class': 'form-control'}),
		}