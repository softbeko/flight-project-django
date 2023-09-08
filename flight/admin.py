from django.contrib import admin
from .models import Campaing


class CampaingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Campaing, CampaingAdmin)
