from django.urls import path
from . import views

app_name = 'fitts'

urlpatterns = [
    path('', views.login, name='login'),
    path('fitts_task/1', views.fitts1, name='fitts1'),
    path('fitts_task/2', views.fitts2, name='fitts2'),
    path('fitts_task/3', views.fitts3, name='fitts3'),
    path('fitts_task/4', views.fitts4, name='fitts4'),
    path('fitts_task/5', views.fitts5, name='fitts5'),
    path('fitts_task/6', views.fitts6, name='fitts6'),
    path('fitts_task/end', views.end, name='end')
]