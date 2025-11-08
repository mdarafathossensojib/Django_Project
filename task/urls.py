from django.urls import path
from .views import *

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),  
    path('user-dashboard/', user_dashboard, name='user-dashboard'),  
    path('test/', test, name='test'),
    path('create-task/', create_task, name='create-task'),
]