# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Restaurant
from api.serializers import RestaurantSerializer

@csrf_exempt
def restaurant_list(request):
    """
    List all code restaurants, or create a new restaurant.
    """
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.

def restaurant_detail(request, pk):
    if request.method == 'GET':
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data, safe=False)
