from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse
from .forms import PostCreateFrom
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateFrom
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-list')


class PostListView(ListView):
    model = Post
    template_name = 'users/post_list.html'
    context_object_name = 'user_post_list'
