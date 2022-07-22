from rest_framework import serializers
from .models import  UbeswapModels

class UbeswapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbeswapModels
        fields ="__all__"