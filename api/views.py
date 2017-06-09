# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.models import Restaurant, Like, Dislike
from api.serializers import RestaurantSerializer, LikeSerializer, DislikeSerializer
import pdb


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key,
                         'username': token.user.username,
                         'user_id': token.user.id,
                         })

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



@api_view(['POST'])
def create_like(request):
    try:
        dislike = Dislike.objects.get(user=request.data.user)
        dislike.delete()

    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_dislike(request):
    try:
        like = Like.objects.get(user=request.data.user)
        like.delete()

    if request.method == 'POST':
        serializer = DislikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
