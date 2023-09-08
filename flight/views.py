from rest_framework import viewsets, serializers
from .models import Campaing


class CampaingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaing
        fields = "__all__"


class CampaingViewSet(viewsets.ModelViewSet):
    queryset = Campaing.objects.all()
    serializer_class = CampaingSerializer
