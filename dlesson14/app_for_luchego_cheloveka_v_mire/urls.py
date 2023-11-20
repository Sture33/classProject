from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('form/', form, name='form'),
    path('detail/<int:pk>', detail, name='detail'),
]
