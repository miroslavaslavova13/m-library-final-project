from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from m_library.accounts.forms import UserCreateForm, UserEditForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('all books')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, *kwargs)

        login(request, self.object)
        return response


class SignInView(LoginView):
    template_name = 'accounts/sign-in.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailsView(DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel


class ProfileEditView(UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = UserModel
    fields = ('username', 'email', 'first_name', 'last_name', 'password', 'avatar')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home')
