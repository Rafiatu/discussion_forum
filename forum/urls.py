from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/", include("posts.urls")),
    path("auth/login", obtain_auth_token),
]
