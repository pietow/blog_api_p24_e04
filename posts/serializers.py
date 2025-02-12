from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at",)
        model = Post