from django.urls import path
from .views import *

urlpatterns = [
    path('createacc',StudentAPI.as_view()),
    path('createacc/<pk>',StudentAPI.as_view()),    
    path('photo/',PhotoAPI.as_view()),
    path('data/',DataRetriveAPI.as_view()),
]
