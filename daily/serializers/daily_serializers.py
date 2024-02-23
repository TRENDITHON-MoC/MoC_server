from rest_framework import serializers
from ..models import Daily

class DateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    class Meta:
        model = Daily
        fields = ['date']