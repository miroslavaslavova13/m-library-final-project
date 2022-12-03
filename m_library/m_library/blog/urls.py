from django.urls import path, include

from m_library.blog.views import blog, PostDetailsView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', blog, name='blog'),
    path('add-post/', AddPostView.as_view(), name='add post'),
    path('<int:pk>/', include([
        path('', PostDetailsView.as_view(), name='post details'),
        path('edit-post/', EditPostView.as_view(), name='edit post'),
        path('delete-post/', DeletePostView.as_view(), name='delete post'),
    ]))
]