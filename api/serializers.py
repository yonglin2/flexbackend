from rest_framework import serializers
from api.models import Restaurant, Like, Dislike

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'place_id', 'lat', 'lng')
    # name = serializers.CharField()
    # place_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Restaurant.objects.create(**validated_data)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'restaurant')

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ('user', 'restaurant')
