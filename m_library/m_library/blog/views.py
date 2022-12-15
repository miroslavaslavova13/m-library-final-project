from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from m_library.blog.forms import PostCreateForm, PostEditForm, PostCommentForm, PostCommentEditForm
from m_library.blog.models import BlogPost, BlogPostComment
from m_library.common.forms import SearchForm


def blog(request):
    posts = BlogPost.objects.all().order_by('-date_of_publication')
    search_form = SearchForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['text']

    if search_pattern:
        posts = posts.filter(
            Q(title__icontains=search_pattern) |
            Q(description__icontains=search_pattern))

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'search_form': search_form,
        'page_obj': page_obj
    }
    return render(request, 'blog/blog.html', context)


class PostDetailsView(DetailView):
    model = BlogPost
    template_name = 'blog/blog-post-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object.user
        context['comments_count'] = self.object.blogpostcomment_set.count()
        context['recent_posts'] = (BlogPost.objects.all()[::-1])[:5]
        context['comment_form'] = PostCommentForm()

        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = PostCreateForm
    template_name = 'blog/add-blog-post.html'
    success_url = reverse_lazy('blog')

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('blog')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = PostEditForm
    template_name = 'blog/edit-blog-post.html'

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/delete-blog-post.html'
    success_url = reverse_lazy('blog')


@login_required
def comment_post(request, post_id):
    post = BlogPost.objects.filter(pk=post_id).get()

    if request.method == "GET":
        form = PostCommentForm()
    else:
        form = PostCommentForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.user = request.user
            comment.save()
            return redirect('post details', pk=post.pk)


class EditCommentView(LoginRequiredMixin, UpdateView):
    model = BlogPostComment
    form_class = PostCommentEditForm
    template_name = 'blog/edit-comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = BlogPostComment.objects.filter(pk=self.object.pk).get().blog_post_id
        return context

    def get_success_url(self):
        return reverse_lazy('post details',
                            kwargs={'pk': BlogPostComment.objects.filter(pk=self.object.pk).get().blog_post_id})


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = BlogPostComment

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('post details',
                            kwargs={'pk': BlogPostComment.objects.filter(pk=self.object.pk).get().blog_post_id})
