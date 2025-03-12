from django.urls import path
from . import views
from .views import commission_list, commission_details

urlpatterns = [
    path('commissions/list', commission_list, name="commission_list"),
    path('commissions/detail/<int:param>', commission_details, name="commission_details"),
    ]

app_name = "commissions"