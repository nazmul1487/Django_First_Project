from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, 'home/index.html', context)
