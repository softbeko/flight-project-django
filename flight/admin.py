from django.contrib import admin
from .models import Campaing
from .models import Logo

class CampaingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Campaing, CampaingAdmin)
admin.site.register(Logo)
