from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View


class AdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    permission_denied_message = 'Only admin has access to this view'

    def test_func(self):
        return self.request.user.is_superuser
