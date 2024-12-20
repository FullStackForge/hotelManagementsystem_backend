from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banners
        fields = ['id','title','image']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['mobile']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email','profile']
        extra_kwargs = {
            'password': {'write_only': True}  # Prevent password from being returned
        }
        
    def create(self,validated_data):
        # Extract the profile data and password from validated_data
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password')

        # Create the User object
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        # Update the Profile associated with the User
        models.Profile.objects.filter(user=user).update(**profile_data)

        return user