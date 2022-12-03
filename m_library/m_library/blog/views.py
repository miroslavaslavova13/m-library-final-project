from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def blog(request):
    return render(request, 'blog/blog.html')


class PostDetailsView(DetailView):
    template_name = 'blog/blog-post-details.html'


class AddPostView(CreateView):
    template_name = 'blog/add-blog-post.html'


class EditPostView(UpdateView):
    template_name = 'blog/edit-blog-post.html'


class DeletePostView(DeleteView):
    template_name = 'blog/delete-blog-post.html'


def comment_post(request):
    return redirect('post details')