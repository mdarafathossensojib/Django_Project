from django.shortcuts import render, redirect
from task.forms import  TaskModelForm, TaskDetailModelForm
from task.models import Task, TaskDetail, Project, Employee
from django.db.models import Q, Count
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required

# Create your views here.

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()


@user_passes_test(is_manager, login_url='no-permission')
def manager_dashboard(request):
    type = request.GET.get('type', 'all')

    counts = Task.objects.aggregate(
        total=Count('id'),
        completed_task=Count('id', filter=Q(status='COMPLETED')),
        pending_task=Count('id', filter=Q(status='PENDING')),
        in_progress_task=Count('id', filter=Q(status='IN_PROGRESS'))
        )
    
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    
    if type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif type == 'in_progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'all':
        tasks = base_query.all()

    context = {
        'tasks': tasks,
        'counts': counts,
    }

    return render(request, 'dashboard/manager-dashboard.html', context)


@user_passes_test(is_employee, login_url='no-permission')
def employee_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

@login_required
@permission_required('task.add_task', login_url='no-permission')
def create_task(request):
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, 'Task created successfully!')
            return redirect('create-task')
        
    context = {'task_form': task_form, 'task_detail_form': task_detail_form}
    return render(request, 'task_form.html', context)

@login_required
@permission_required('task.change_task', login_url='no-permission')
def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    task_detail_form = TaskDetailModelForm(instance=task.details)

    if request.method == 'POST':
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, 'Task Updated successfully!')
            return redirect('update-task')
        
    context = {'task_form': task_form, 'task_detail_form': task_detail_form}
    return render(request, 'task_form.html', context)

@login_required
@permission_required('task.delete_task', login_url='no-permission')
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('manager-dashboard')

@login_required
@permission_required('task.view_task', login_url='no-permission')
def view_task(request):
    tasks = Task.objects.filter(status='PENDING')

    return render(request, 'show_task.html', {'tasks' : tasks})