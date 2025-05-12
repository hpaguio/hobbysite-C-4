from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    CartView,
    TransactionListView
    )

app_name = "merchstore"

urlpatterns = [
    path("", lambda request: HttpResponseRedirect(reverse_lazy("merchstore:product-list"))),
    path("items", ProductListView.as_view(), name='product-list'),
    path("item/<int:pk>", ProductDetailView.as_view(), name='product-detail'),
    path("item/add", ProductCreateView.as_view(success_url=reverse_lazy('merchstore:product-list')), name='product-create'),
    path("item/<int:pk>/edit", ProductUpdateView.as_view(success_url=reverse_lazy('merchstore:product-list')), name='product-edit'),
    path("cart", CartView.as_view(), name='cart-list'),
    path("transactions", TransactionListView.as_view(), name='transaction-list')
]