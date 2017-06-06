# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    place_id = models.IntegerField()


class Like(models.Model):
    user = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    created = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
