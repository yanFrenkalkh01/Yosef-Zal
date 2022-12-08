from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(view_func):  # User authentication
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):  # Allow only selected type of users
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func
    return decorator


def user_redirect(view_func):  # Redirect users to the correct page
    def wrapper_func(request, *args, **kwargs):
        # Make group var
        group = None
        if request.user.groups.exists():  # Chak if the user is in a group
            group = request.user.groups.all()[0].name   # Get the group name
        # redirect the user according to the group
        if group == 'Doctor':
            return redirect('Doctor/')

        if group == 'Patient':
            return redirect('Patient/')

        if group == 'Administrator':
            return redirect('Administrator/')

    return wrapper_func

