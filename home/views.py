from django.shortcuts import render

# default view  of the home apps
def index(request, *args, **kwargs):
    context = {}
    return render(request, 'home/index.html', context)
