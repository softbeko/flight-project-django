from django.urls import path
from . import views


urlpatterns = [
    path("campaing/", views.CampaingViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "campaing/<int:pk>/",
        views.CampaingViewSet.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
    ),
]
