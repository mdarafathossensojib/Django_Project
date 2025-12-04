from django.urls import path
from task.views import dashboard, ManagerDashboardView, EmployeeDashboardView, CreateTaskView, UpdateTask, ViewProject, TaskDetail, ViewTask, DeleteTaskView

urlpatterns = [
    path('manager-dashboard/', ManagerDashboardView.as_view(), name='manager-dashboard'),  
    path('user-dashboard/', EmployeeDashboardView.as_view(), name='user-dashboard'),  
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete-task'),
    path('view-task/', ViewTask.as_view(), name='view-task'),
    path('view-project/', ViewProject.as_view(), name='view-project'),
    path('details/<int:task_id>/', TaskDetail.as_view(), name='task-details'),
    path('dashboard/', dashboard, name='dashboard'),
]