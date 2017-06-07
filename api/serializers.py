from rest_framework import serializers
from api.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'place_id', 'lat', 'lng')
    # name = serializers.CharField()
    # place_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Restaurant.objects.create(**validated_data)
