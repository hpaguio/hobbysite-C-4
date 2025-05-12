from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from .models import ProductType, Product, Transaction
from .forms import TransactionForm
from user_management.models import Profile

class ProductListView(ListView):
	model = Product
	template_name = 'product_list.html'
	context_object_name = 'products'


class ProductDetailView(DetailView):
	model = Product
	template_name = 'product_detail.html'
	context_object_name= 'product'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		product = self.get_object()
		context['transaction_form'] = TransactionForm()

		return context

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect("login")

		self.object = self.get_object()
		profile = get_object_or_404(Profile, user=request.user)
		form = TransactionForm(request.POST)

		if form.is_valid():
			transaction = form.save(commit=False)
			transaction.buyer = profile
			transaction.product = self.object
			transaction.save()
			return redirect("merchstore:cart-list")

		context = self.get_context_data()
		context["transaction_form"] = form
		return self.render_to_response(context)


class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	template_name = 'product_form.html'
	fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']

	def form_valid(self, form):
		form.instance.owner = get_object_or_404(Profile, user=self.request.user)
		return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	template_name = 'product_form.html'
	fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']

	def test_func(self):
		product = self.get_object()
		return product.owner.user == self.request.user


class CartView(LoginRequiredMixin, ListView):
	model = Transaction
	template_name = 'cart_list.html'
	context_object_name = 'cart'

	def get_queryset(self):
		return Transaction.objects.filter(buyer__user__exact=self.request.user)


class TransactionListView(LoginRequiredMixin, ListView):
	model = Transaction
	template_name = 'transaction_list.html'
	context_object_name = 'transactions'

	def get_queryset(self):
		return Transaction.objects.filter(product__owner__user__exact=self.request.user)