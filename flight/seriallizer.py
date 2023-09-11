from rest_framework import serializers
from .models import Campaings


class CampaingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaings
        fields = "__all__"
