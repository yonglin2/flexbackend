# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Restaurant
from api.serializers import RestaurantSerializer

@api_view(['GET', 'POST'])
def restaurant_list(request):
    """
    List all restaurants, or create a new restaurant.
    """
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        # restaurants_dict = {}
        # for restaurant in restaurants:
        #     restaurants_dict[restaurant.id] = restaurant
        #     print restaurant
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=request.data)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx')
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Create your views here.

def restaurant_detail(request, pk):

    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(restaurant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        restaurant.delete()
        return HttpResponse(status=204)
