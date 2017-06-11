from api.models import Restaurant, Like, Dislike
from django.contrib.auth.models import User

Like.objects.all().delete()
Dislike.objects.all().delete()
