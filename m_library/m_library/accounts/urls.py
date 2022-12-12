from django.contrib.auth.decorators import login_required
from django.urls import path, include

from m_library.accounts.views import SignUpView, SignInView, SignOutView, ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/<int:pk>/', include([
        path('', login_required(ProfileDetailsView.as_view()), name='profile details'),
        path('edit/', login_required(ProfileEditView.as_view()), name='edit profile'),
        path('delete/', login_required(ProfileDeleteView.as_view()), name='delete profile')
    ]))

]
