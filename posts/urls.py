from django.urls import path
from .views import (
    PostCreateView,
    PostUpdateView,
    PostListView,
    PostDeleteView,
    CommentCreateView,
)


urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('create',  PostCreateView.as_view(), name="post-create"),
    path('<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),

    path('<int:post_id>/comments/create', CommentCreateView.as_view(), name="comment-create")
]
