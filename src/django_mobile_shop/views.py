from django.shortcuts import render


def home(request):
    title = 'Welcome to DMS'
    context = {'title': title}
    return render(request, 'index.html', context)
