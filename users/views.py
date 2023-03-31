from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User

    fields = [
        "username",
        "name",
        "bio",
    ]


    def get_success_url(self):
        return reverse("home")

    def get_object(self):
        return User.objects.get(username=self.request.user.username)