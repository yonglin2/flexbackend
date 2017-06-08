from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^restaurants/$', views.restaurant_list),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.restaurant_detail),
    url(r'^api-token-auth/', views.CustomObtainAuthToken.as_view()),
]
