from django.shortcuts import render
from django.http import HttpResponse

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')