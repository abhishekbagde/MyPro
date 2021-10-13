from django.urls import path
from . import views

#URLCOnfig
urlpatterns = [
    path('', views.say_hello)
]