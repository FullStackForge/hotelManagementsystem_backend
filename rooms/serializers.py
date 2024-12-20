from rest_framework import serializers
from . import models
class RoomTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomImage
        fields = ['image']
class RoomTypeSerializer(serializers.ModelSerializer):
    room_type_imgs = RoomTypeImageSerializer(many=True,read_only=True)
    class Meta:
        model = models.RoomType
        fields = ['uuid','title','detail','room_type_imgs']