from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
    To edit the render of the navbar depended on the page
    edd fields to the dictionary NavBarRender in the next format:
        'varType': {'pageType': 'arg'}
'''

NavBarRender = {
    'dashboard': {'pageType': 'dashboard'},
    'home': {'pageType': 'home'},
}


def dashboard(request):
    return render(request, 'accounts/dashboard.html', NavBarRender['dashboard'])


def home(request):
    return render(request, 'accounts/home.html', NavBarRender['home'])

