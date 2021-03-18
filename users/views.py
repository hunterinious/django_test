from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from users.forms import UserCreateForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = 'auth/registration.html'

    def get_success_url(self):
        return reverse('sign-up')
