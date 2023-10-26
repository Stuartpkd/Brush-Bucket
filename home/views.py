from django.shortcuts import render


def index(request):
    """ A view to return the home index page """

    return render(request, 'home/index.html')
