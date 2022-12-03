from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'


class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailsView(DetailView):
    template_name = 'accounts/profile-details.html'


class ProfileEditView(UpdateView):
    template_name = 'accounts/edit-profile.html'


class ProfileDeleteView(DeleteView):
    template_name = 'accounts/delete-profile.html'
