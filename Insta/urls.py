from django.contrib import admin
from django.urls import path, include

from Insta.views import HelloWorld, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("test/", HelloWorld.as_view(), name="helloworld"),
    path("posts/", PostView.as_view(), name="posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="make_post"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="update_detail"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="delete_detail"),
]