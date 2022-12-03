from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('m_library.common.urls')),
    path('accounts/', include('m_library.accounts.urls')),
    path('books/', include('m_library.books.urls')),
    path('blog/', include('m_library.blog.urls')),

]
