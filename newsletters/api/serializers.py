from rest_framework import serializers
from ..models import Newsletter


class News_serializers(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
