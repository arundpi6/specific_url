from app2.views import *
from django.urls import path
app_name='yes'

urlpatterns = [
    path('html_app2/',html_app2,name='html_app2'),
]