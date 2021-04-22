from rest_framework import serializers
from ..models import Post


class Post_serializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'updated_on', 'content', 'created_on', 'status')
