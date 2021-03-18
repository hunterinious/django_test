from django import forms
from posts.models import Post


class PostCreateFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('theme', 'description', 'picture')
