from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from . import serializers
from . import models
from django.contrib.auth.models import User
# Create your views here.

class BannersList(ListAPIView):
    serializer_class = serializers.BannerSerializer
    queryset = models.Banners.objects.all()

class UserCreateView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()