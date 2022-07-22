from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import  UbeswapSerializer
from .models import UbeswapModels
from rest_framework import viewsets

# Create your views here.
class UbeListView(viewsets.ModelViewSet):
    serializer_class =  UbeswapSerializer
    queryset = UbeswapModels.objects.all()
    

