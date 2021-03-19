from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
