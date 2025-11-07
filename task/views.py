from django.shortcuts import render

# Create your views here.

def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')


def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    context = {
        'names' : ["Mohammad", "Arafat", "Hossen", "Sojib"]
    }
    return render(request, 'test.html', context)