from rest_framework import serializers
from api.models import Restaurant

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField()
    place_id = serializers.IntegerField()

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
