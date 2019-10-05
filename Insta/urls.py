from django.contrib import admin
from django.urls import path, include

from Insta.views import HelloWorld

urlpatterns = [
    path("", HelloWorld.as_view(), name="home"),
]
