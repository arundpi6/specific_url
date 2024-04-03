from app3.views import *
from django.urls import path
app_name='yes_noo'

urlpatterns = [
    path('html_app3/',html_app3,name='html_app3'),
]