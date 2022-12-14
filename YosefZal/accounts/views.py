from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .decorators import authenticated_user, allowed_users, user_redirect


'''
    To edit the render of the navbar depended on the page
    edd fields to the dictionary NavBarRender in the next format:
        'varType': {'pageType': 'arg'}
'''

NavBarRender = {
    'patient': {'pageType': 'Patient'},
    'doctor': {'pageType': 'Doctor'},
    'administrator': {'pageType': 'Administrator'},
    'home': {'pageType': 'home'},
    'go_find': {'pageType': 'go_find'},
}


def home(request):
    # Home page
    return render(request, 'accounts/home.html', NavBarRender['home'])


def go_find(request):
    # go find page
    return render(request, 'accounts/go_find.html', NavBarRender['go_find'])


@authenticated_user
def register_page(request):  # User registration page
    # Generate default user creation form from django
    form = CreateUserForm()

    # check for POST request
    if request.method == 'POST':
        # Get form from user creation form
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # save user details in user var
            user = form.save()
            # Get username from registration
            username = form.cleaned_data.get('username')
            # Get group from group list
            group = Group.objects.get(name='Patient')
            # Add user to grop
            user.groups.add(group)

            messages.success(request, 'Account was crated for' + username)
            # Redirect to login page if the registration was successful
            return redirect('login')
    # insert the form in to dictionary to assignee in to the HTML files
    context = {'form': form, 'pageType': 'register'}
    # Render the html content
    return render(request, 'accounts/auth/register.html', context)


@authenticated_user
def login_page(request):   # User sing in
    # check for POST request
    if request.method == 'POST':
        # Get username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate the username and password
        user = authenticate(request, username=username, password=password)

        # if user exist login the user and redirect to users middle page
        if user is not None:
            login(request, user)
            return redirect('users')
        else:
            # message to indicate if thar is a wrong username or password
            messages.info(request, 'Username OR password is incorrect')

    context = {'pageType': 'login'}
    # Render the login page html file
    return render(request, 'accounts/auth/login.html', context)


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
def logout_user(request):   # Logout page
    # logout the user
    logout(request)
    # Redirect to home page
    return redirect('home')


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Administrator'])  # Use costume decorator to allow only authenticated user type.
def dashboard(request):
    return render(request, 'accounts/dashboard.html', NavBarRender['dashboard'])


# Redirecting page
@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@user_redirect   # Use costume decorator redirect users based on user type.
def users(request):
    return HttpResponse("ERROR 404 you dont cant be in that page")  # massage if the user entered forbidden page


@login_required(login_url='login')
@xframe_options_exempt
def profile(request):
    return render(request, 'accounts/users/profile.html')


@login_required(login_url='login')
@xframe_options_exempt
def note(request):
    return render(request, 'accounts/users/note.html')


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Doctor'])   # Use costume decorator to allow only authenticated user type.
def user_doctor(request):  # Costume Doctor page
    return render(request, 'accounts/users/Doctor.html', NavBarRender['doctor'])


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Patient'])   # Use costume decorator to allow only authenticated user type.
def user_patient(request):  # Costume Patient page
    return render(request, 'accounts/users/Patient.html', NavBarRender['patient'])


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Administrator'])   # Use costume decorator to allow only authenticated user type.
def user_admin(request):  # Costume Administrator page
    return render(request, 'accounts/users/Administrator.html', NavBarRender['administrator'])