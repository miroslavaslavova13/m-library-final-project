from django.contrib.auth import get_user_model
from django.test import TestCase

from m_library.blog.forms import PostDeleteForm, PostCommentDeleteForm
from m_library.blog.models import BlogPost, BlogPostComment

UserModel = get_user_model()

class BlogPostDeleteFormTests(TestCase):
    def test_blog_post_delete_form_fields_are_disabled(self):
        form = PostDeleteForm()
        disabled_fields = {name: field.widget.attrs['readonly'] for name, field in form.fields.items()}

        self.assertEqual('readonly', disabled_fields['title'])

        self.assertEqual('readonly', disabled_fields['description'])


    def test_blog_post_delete_form_save_method_deletes_the_book_successfully(self):
        credentials = {
            'username': 'some_username123',
            'password': '@SomePassword123'
        }
        user = UserModel.objects.create(**credentials)

        blog_post = BlogPost.objects.create(
            title='Some title',
            description='Short description of the post',
            user=user
        )

        form = PostDeleteForm(instance=blog_post)
        form.save()

        self.assertNotIn(blog_post, BlogPost.objects.all())
        self.assertEqual(0, len(BlogPost.objects.all()))



class PostCommentDeleteFormTests(TestCase):
    # can add more test if there are more comments and deletes the right one
    def test_post_comment_delete_form_save_method_deletes_comment_successfully(self):
        credentials = {
            'username': 'some_username123',
            'password': '@SomePassword123'
        }
        user = UserModel.objects.create(**credentials)

        blog_post = BlogPost.objects.create(
            title='Some title',
            description='Short description of the post',
            user=user
        )

        blog_post_comment = BlogPostComment.objects.create(
            text='Some text',
            blog_post=blog_post,
            user=user
        )

        form = PostCommentDeleteForm(instance=blog_post_comment)
        form.save()

        self.assertNotIn(blog_post, BlogPostComment.objects.all())
        self.assertEqual(0, len(BlogPostComment.objects.all()))