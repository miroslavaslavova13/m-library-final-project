from django.urls import path, include

from m_library.blog.views import blog, PostDetailsView, AddPostView, EditPostView, DeletePostView, comment_post, \
    EditCommentView, DeleteCommentView

urlpatterns = [
    path('', blog, name='blog'),
    path('comment/<int:post_id>/', comment_post, name='comment post'),
    path('<int:post_id>/edit-comment/<int:pk>/', EditCommentView.as_view(), name='edit comment'),
    path('<int:post_id>/delete-comment/<int:pk>/', DeleteCommentView.as_view(), name='delete comment'),

    path('add-post/', AddPostView.as_view(), name='add post'),
    path('<int:pk>/', include([
        path('', PostDetailsView.as_view(), name='post details'),
        path('edit-post/', EditPostView.as_view(), name='edit post'),
        path('delete-post/', DeletePostView.as_view(), name='delete post'),
    ]))
]
