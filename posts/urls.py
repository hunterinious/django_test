from django.urls import path
from .views import PostCreateView, PostListView


urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('create',  PostCreateView.as_view(), name="create-post"),
]