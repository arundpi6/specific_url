from app1.views import *
from django.urls import path
app_name='noo'

urlpatterns = [
    path('str_app1/',str_app1,name='str_app1'),
]