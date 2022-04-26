from rest_framework import authentication
from mytrueweight.models import Weight
from .serializers import WeightSerializer
from rest_framework import viewsets


class WeightViewSet(viewsets.ModelViewSet):
    serializer_class = WeightSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Weight.objects.all()
