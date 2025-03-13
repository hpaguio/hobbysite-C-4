from django.urls import path
from .views import commission_list, commission_details

app_name = "commissions"

urlpatterns = [
    path("", commission_list, name="commission_home"),  # ✅ Default route
    path("list/", commission_list, name="commission_list"),
    path("detail/<int:param>/", commission_details, name="commission_details"),
]