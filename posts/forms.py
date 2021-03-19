from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('theme', 'description', 'picture')


class ComemntForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', )
