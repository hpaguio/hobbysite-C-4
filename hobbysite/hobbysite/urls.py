from django.contrib import admin
from django.urls import path, include
from user_management.views import home_view

from django.conf import settings  # ➔ add
from django.conf.urls.static import static  # ➔ add

urlpatterns = [
    path("admin/", admin.site.urls),

    # Core apps
    path("forum/", include("forum.urls")),
    path("commissions/", include("commissions.urls")),
    path("blog/", include("blog.urls")),
    path("wiki/", include("wiki.urls")),
    path("merchstore/", include("merchstore.urls")),

    # Authentication (Login, Logout, Password)
    path("accounts/", include("django.contrib.auth.urls")),

    # User management (registration, profile, etc.)
    path("accounts/", include("user_management.urls")),

    # Root route redirects to the custom homepage
    path("", home_view, name="home"),
]

# ➔ serve media files (uploads) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)