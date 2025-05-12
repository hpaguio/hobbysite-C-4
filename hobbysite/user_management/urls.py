from django.urls import path
from . import views

app_name = "user_management"

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_update, name="profile-update"),
    path("register/", views.register, name="register"),
]
