from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, login, authenticate
from users.forms import UserCreateForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(self.request, user)
            return redirect('post-list')

        return super(SignUpView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-list')
