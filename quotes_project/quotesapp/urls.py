from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.index, name='index'),
]
