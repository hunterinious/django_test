from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import PostForm, ComemntForm
from .models import Post
from core.views import AdminOnlyView


class OnlyAuthorCanUpdate(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only author can update this post'

    def test_func(self):
        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, id=post_id)
        return self.request.user == post.user


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(OnlyAuthorCanUpdate, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    form_class = PostForm
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-update', kwargs={'pk': self.kwargs['pk']})


class PostDeleteView(AdminOnlyView, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = ComemntForm
    template_name = 'posts/comments/comment_create.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post
        return super(CommentCreateView, self).form_valid(form)
