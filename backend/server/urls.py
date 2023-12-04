from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api/", include([])),
    path('adminpanel/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
]
