from rest_framework import serializers

from .models import PersonalDetails


class PersonalDetailsSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    address=serializers.TextField()
    contact_number=serializers.IntegerField()
    class Meta:
        model=PersonalDetails
        fields='__all__'