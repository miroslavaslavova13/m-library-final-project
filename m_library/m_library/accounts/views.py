from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from m_library.accounts.forms import UserCreateForm
from m_library.books.models import BookFavourite

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('all books')

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('all books')
        return super().post(request, *args, **kwargs)


class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'

    def get_success_url(self):
        return reverse_lazy('all books')


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def test_func(self):
        return self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_favourite_books'] = BookFavourite.objects.filter(user_id=self.request.user.pk)

        return context


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = UserModel
    fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    def test_func(self):
        return self.get_object() == self.request.user

    # TODO change status code to 404 and render 404.html

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object() == self.request.user
    # TODO change status code to 404 and render 404.html
