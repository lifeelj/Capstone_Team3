from django.urls import path
from . import views

app_name = 'fitts'

urlpatterns = [
    path('fitts_task', views.fitts, name='fitts'),
]