from django.urls import path
from. import views

urlpatterns = [
    path('', views.cascade, name="cascade"),
    path('sub', views.person, name="person"),
    ]