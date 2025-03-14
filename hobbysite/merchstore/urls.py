from django.urls import path
from .views import merchstore_list, merchstore_detail

app_name = "merchstore"

urlpatterns = [
    path("", merchstore_list, name="merchstore_home"),
    path("list/", merchstore_list, name="merchstore_list"),
    path("item/<int:param>/", merchstore_detail, name="merchstore_detail"),
]