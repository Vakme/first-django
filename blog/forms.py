
from captcha.fields import ReCaptchaField
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        captcha = ReCaptchaField()
        fields = ('author', 'text',)

