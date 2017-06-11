# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    place_id = models.CharField(max_length=500)
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(blank=True, max_length=200)
    phone_number = models.CharField(blank=True, max_length=50)
    image_url = models.CharField(max_length=200, default='')
    # user_likes = models.ManyToManyField(User, related_name='restaurant_likes', through)
    # user_dislikes = models.ManyToManyField(User, related_name='restaurant_dislikes')

    def __str__(self):
        return self.name

# Like.objects.create(user=yong, restaurant=tokyo)

# TODO: change likes/dislikes model to have id's instead of objects
# TODO: In restaurant model, add address, phone_number, array of likers id, array of dislikers id

class Like(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, related_name='likes')
    user = models.ForeignKey(User, related_name='liker')

class Dislike(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, related_name='dislikes')
    user = models.ForeignKey(User, related_name='disliker')

# class Like(models.Model):
#     user = models.ForeignKey(User)
#     restaurant = models.ForeignKey(Restaurant)
#     created = models.DateTimeField(auto_now_add=True)
#
# class Dislike(models.Model):
#     user = models.ForeignKey(User)
#     restaurant = models.ForeignKey(Restaurant)
#     created = models.DateTimeField(auto_now_add=True)

# Create your models here.
