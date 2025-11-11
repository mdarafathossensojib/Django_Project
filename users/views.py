from django.shortcuts import render


def sign_up(request):
    return render(request, 'registration/registration.html')