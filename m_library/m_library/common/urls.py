from django.urls import path

from m_library.common.views import index

urlpatterns = [
    path('', index, name='home')
]