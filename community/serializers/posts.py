from rest_framework import serializers

from community.models import Post, PostView


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = "__all__"
