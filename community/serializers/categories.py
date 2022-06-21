from rest_framework import serializers

from community.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        ref_name = "CommunityCategorySerializer"
