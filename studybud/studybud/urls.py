from django.contrib import admin
from django.urls import path, include

# Here is the root URL configuration for the project.
# URLS trigger views(controllers), which return responses.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]
