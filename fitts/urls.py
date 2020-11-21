from django.urls import path
from . import views

app_name = 'fitts'

urlpatterns = [
    path('', views.login, name='login'),
    path('fitts_task', views.fitts, name='fitts'),
]