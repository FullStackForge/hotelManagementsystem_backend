from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import serializers
from . import models
# Create your views here.
class RoomTypeListView(ListAPIView):
    serializer_class = serializers.RoomTypeSerializer
    queryset = models.RoomType.objects.all()

class RoomTypeDetailView(RetrieveAPIView):
    serializer_class = serializers.RoomTypeSerializer
    queryset = models.RoomType.objects.all()
    lookup_field='uuid'