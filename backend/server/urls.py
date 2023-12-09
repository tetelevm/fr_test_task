from django.contrib import admin
from django.urls import path, include


service_urls = [
    path("adminpanel/", admin.site.urls),
    path("select2/", include("django_select2.urls")),
]


urlpatterns = [
    path("api/", include([])),
    path("service/", include(service_urls)),
]
