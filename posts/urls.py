from django.urls import path
from .views import PostCreateView, PostUpdateView, PostListView


urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('create',  PostCreateView.as_view(), name="post-create"),
    path('<int:pk>/update', PostUpdateView.as_view(), name="post-update")
]