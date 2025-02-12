from django.db import models
from accounts.models import CustomUser
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)