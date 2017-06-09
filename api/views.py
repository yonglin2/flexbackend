# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.models import Restaurant
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from api.serializers import RestaurantSerializer, UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key,
                         'username': token.user.username,
                         'user_id': token.user.id,
                         })

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def create_user(request):
    serialized = UserSerializer(data=request.data, context={'request': request})
    if serialized.is_valid():
        #new user
        user = User(
            username=request.data['username'],
            email=request.data['email'],
        )
        user.set_password(request.data['password'])
        user.save()
        serialized = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=serialized.instance)
        return Response({'user': serialized.data, 'token': token.key}, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def restaurant_list(request):
    """
    List all restaurants, or create a new restaurant.
    """
    if request.method == 'GET':
        # restaurants = Restaurant.objects.all()

        # .015 lat/lng unit ~ 1 mile

        north = float(request.GET['lat']) + .015
        east = float(request.GET['lng']) + .015
        south = float(request.GET['lat']) - .015
        west = float(request.GET['lng']) - .015

        # north = 2000
        # east = 2000
        # south = 50
        # west = 50


        # location filtering
        restaurants = Restaurant.objects.filter(
            lat__lte=north
            ).filter(
            lat__gte=south
            ).filter(
            lng__lte=east
            ).filter(
            lng__gte=west
            )

        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):

    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        restaurant.delete()
        return HttpResponse(status=204)
