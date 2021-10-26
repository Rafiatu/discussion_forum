from django.contrib.auth.models import User
from django.db import models
import uuid


class Post(models.Model):
    id = models.CharField(max_length=200, unique=True, default=uuid.uuid4().hex, editable=False, primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def likes(self):
        return self.liked_by.all().count()
