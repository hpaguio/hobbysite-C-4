from django.urls import path
from . import views
from .views import (
commission_list,
commission_details,
commission_create,
commission_update,
commission_jobview,
commission_jobapply,
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


app_name = "commissions"


urlpatterns = [
    path("", lambda request: HttpResponseRedirect(reverse_lazy("commissions:commission_list"))),
    path("list/", commission_list, name="commission_list"),
    path("detail/<int:param>/", commission_details, name="commission_details"),
    path("add/", commission_create, name="commission_create"),
    path("<int:param>/edit/", commission_update, name="commission_update"),
    path("job/<int:job_id>/", commission_jobview, name="commission_jobview"),
    path("job/<int:job_id>/apply/", commission_jobapply, name="commission_jobapply"),
]