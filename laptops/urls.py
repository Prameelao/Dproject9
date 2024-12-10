from django.urls import path
from laptops.views import*
app_name='laptops'

urlpatterns=[
    path('dell/',dell,name='dell'),
]