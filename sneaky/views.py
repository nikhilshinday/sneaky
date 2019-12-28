from django.shortcuts import render


def index(request):
    return render(request, 'sneaky/index.html')


def energy(request):
    return render(request, 'sneaky/energy.html')


def people(request):
    return render(request, 'sneaky/people.html')


def being(request):
    return render(request, 'sneaky/being.html')
