from django.contrib.auth.decorators import login_required
from django.urls import path, include

from m_library.blog.views import blog, PostDetailsView, AddPostView, EditPostView, DeletePostView, comment_post

urlpatterns = [
    path('', blog, name='blog'),
    path('comment/<int:post_id>/', comment_post, name='comment post'),
    path('add-post/', login_required(AddPostView.as_view()), name='add post'),
    path('<int:pk>/', include([
        path('', PostDetailsView.as_view(), name='post details'),
        path('edit-post/', login_required(EditPostView.as_view()), name='edit post'),
        path('delete-post/', login_required(DeletePostView.as_view()), name='delete post'),
    ]))
]