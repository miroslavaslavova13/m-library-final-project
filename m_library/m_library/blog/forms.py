from django import forms

from m_library.blog.models import BlogPost, BlogPostComment
from m_library.core.form_mixin import DisabledFormMixin


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'description')


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(DisabledFormMixin, PostBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            BlogPostComment.objects.filter(blog_post_id=self.instance.id).delete()

            self.instance.delete()

        return self.instance


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                }
            )
        }


class PostCommentEditForm(PostCommentForm):
    pass


class PostCommentDeleteForm(PostCommentForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
