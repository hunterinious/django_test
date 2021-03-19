from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import PostForm, ComemntForm
from .models import Post
from core.views import AdminOnlyView


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-list')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    form_class = PostForm
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, id=post_id)
        if self.request.user != post.user:
            raise PermissionDenied("You cannot update someone else's post")
        return post

    def get_success_url(self):
        return reverse('post-update', kwargs={'pk': self.kwargs['pk']})


class PostDeleteView(AdminOnlyView, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'user_post_list'


class CommentCreateView(CreateView):
    form_class = ComemntForm
    template_name = 'posts/comments/comment_create.html'

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        if form.is_valid():
            form.instance.post = post
            form.save()
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-list')
