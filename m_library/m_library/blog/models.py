from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import RESTRICT

UserModel = get_user_model()


class BlogPost(models.Model):
    MAX_TITLE_LEN = 100

    title = models.CharField(max_length=MAX_TITLE_LEN, null=False, blank=False)

    description = models.TextField(null=False, blank=False)

    date_of_publication = models.DateField(auto_now=True, null=False, blank=True)

    user = models.ForeignKey(UserModel, on_delete=RESTRICT)


class BlogPostComment(models.Model):
    text = models.TextField(null=False, blank=False)

    publication_date_and_time = models.DateTimeField(auto_now_add=True, blank=True, null=False)

    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False, blank=True)

    user = models.ForeignKey(UserModel, on_delete=RESTRICT)

