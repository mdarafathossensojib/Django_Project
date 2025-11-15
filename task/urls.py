from django.urls import path
from task.views import manager_dashboard, employee_dashboard, create_task, update_task, delete_task, view_task

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),  
    path('user-dashboard/', employee_dashboard, name='user-dashboard'),  
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('view-task/', view_task, name='view-task'),
]