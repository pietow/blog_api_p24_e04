from django.contrib.auth import get_user_model
# from accounts.models import CustomUser
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at",)
        model = Post

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "username",)
        model = get_user_model()