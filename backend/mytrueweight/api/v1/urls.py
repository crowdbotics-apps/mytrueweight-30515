from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import WeightViewSet

router = DefaultRouter()
router.register("weight", WeightViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
