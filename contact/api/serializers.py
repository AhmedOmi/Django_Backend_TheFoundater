from rest_framework import serializers
from ..models import Contact


class Contact_serializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
