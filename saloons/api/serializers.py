from rest_framework import serializers
from saloons.models import Saloon

class SaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = ('__all__')
