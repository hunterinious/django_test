from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import PostCreateFrom


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateFrom
    template_name = 'posts/post_create.html'
