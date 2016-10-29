from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Comment(models.Model):
    post_id = models.ForeignKey('Post')
    author = models.CharField(max_length=100, null=False)
    text = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.text


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def countComments(self):
        return Comment.objects.filter(post_id = self.pk).count()

    def returnShort(self):
        return self.text[:50] + "..."