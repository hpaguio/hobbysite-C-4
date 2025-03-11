from django.urls import path
from . import views
from .views import commission_list, comment_list

urlpatterns = [
    path('commissions/list', commission_list, name="commission_list"),
    path('commissions/detail/<int:param>', comment_list, name="comment_list"),
    ]

app_name = "commissions"