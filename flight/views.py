from rest_framework import viewsets, serializers
from .models import Campaing
from .models import Campaings
from .seriallizer import CampaingsSerializer
from .models import Logo


class CampaingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaing
        fields = "__all__"


class CampaingViewSet(viewsets.ModelViewSet):
    queryset = Campaing.objects.all()
    serializer_class = CampaingSerializer


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ("id", "title", "description", "logo", "searchbackground")


class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class CampaingsViewSet(viewsets.ModelViewSet):
    queryset = Campaings.objects.all()
    serializer_class = CampaingsSerializer
