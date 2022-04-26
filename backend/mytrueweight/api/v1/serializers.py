from rest_framework import serializers
from mytrueweight.models import Weight


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = "__all__"
