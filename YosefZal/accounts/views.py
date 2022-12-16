from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.
from chatrooms.models import ChatRoom
from .models import *
from .forms import CreateUserForm, DocumentForm, UpdateUserForm, UpdateProfileForm, GenerateEvent, EditEventDescription, MakeComplaint
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

            messages.success(request, 'Account was crated for ' + username)
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


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/auth/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users')


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
    query_set = Group.objects.filter(user=request.user)
    return render(request, 'accounts/users/profile.html', {'grups': query_set[0]})


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {'user_form': user_form,
               'profile_form': profile_form,
               'pageType': 'edit_profile'}
    return render(request, 'accounts/users/edit_profile.html', context)


@login_required(login_url='login')
@xframe_options_exempt
def note(request):
    return render(request, 'accounts/users/note.html')


@login_required(login_url='login')
def appointment(request):
    if request.method == 'POST':
        event_form = GenerateEvent(request.POST, instance=UserEvent(patient=request.user.profile))
        if event_form.is_valid():
            event_form.instance.event_name = request.user.username + ' meting'
            event_form.save()
            messages.success(request, 'The appointment was crated successfully')
            return redirect(to='users')
    else:
        event_form = GenerateEvent(instance=UserEvent(patient=request.user.profile))
    group = Group.objects.get(name='Doctor')
    user = group.user_set.all()
    context = {'doctor': user,
               'event_form': event_form
               }
    return render(request, 'accounts/appointment.html', context)


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Doctor'])   # Use costume decorator to allow only authenticated user type.
def user_doctor(request):  # Costume Doctor page
    return render(request, 'accounts/users/Doctor.html', NavBarRender['doctor'])


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Patient'])   # Use costume decorator to allow only authenticated user type.
def user_patient(request):

    return render(request, 'accounts/users/Patient.html', NavBarRender['patient'])


@login_required(login_url='login')  # Use of Django decorator to let only logged on users in the page
@allowed_users(allowed_roles=['Administrator'])   # Use costume decorator to allow only authenticated user type.
def user_admin(request):  # Costume Administrator page
    return render(request, 'accounts/users/Administrator.html', NavBarRender['administrator'])


@login_required(login_url='login')
def user_chat_room(request):
    context = {'pageType': 'chatRoom'}
    return render(request, 'accounts/users/chatroom.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctor'])
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('accounts.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'accounts/upload/list.html',
        {'documents': documents, 'form': form, 'pageType': 'upload'},
    )


@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctor'])
def doctor_prescriptions(request):
    context = {'pageType': 'prescriptions'}
    return render(request, 'accounts/prescriptions.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Doctor'])
def doctor_history(request):
    room = ChatRoom.objects.first()
    room_name = room.name
    user = room_name.split(request.user.username)
    patient = Profile.objects.filter(profile_number=user[0])
    events = UserEvent.objects.filter(patient=patient[0], doctor=request.user.username)
    if request.method == "POST":
        description = EditEventDescription(request.POST, instance=events.first())
        if description.is_valid():
            description.save()
            messages.success(request, 'The description was crated successfully')
            return redirect(to='meetings')
    else:
        description = EditEventDescription(instance=events.first())

    context = {'pageType': 'prescriptions',
               'events': events,
               'description': description,
               'patient': patient[0]}
    return render(request, 'accounts/history.html', context)


@login_required(login_url='login')
def meting_list(request):
    group = request.user.groups.get()
    print(group)
    if str(request.user.groups.get()) == 'Doctor':
        meetings = UserEvent.objects.filter(doctor=request.user.username)
    else:
        meetings = UserEvent.objects.filter(patient=request.user.profile)
    context = {'pageType': 'meetings',
               'list': meetings,
               'group': str(group)}
    return render(request, 'accounts/meting_list.html', context)


@login_required(login_url='login')
def complaint_ticket(request):
    group = request.user.groups.get()
    if request.method == "POST":
        complaint_form = MakeComplaint(request.POST, instance=UserComplaints(profile=request.user.profile))
        if complaint_form.is_valid():
            complaint_form.save()
            messages.success(request, 'The complaint was crated successfully')
            return redirect(to='users')
    else:
        complaint_form = MakeComplaint(instance=UserComplaints(profile=request.user.profile))

    context = {'pageType': 'complaint',
               'group': str(group),
               'complaint_form': complaint_form}
    return render(request, 'accounts/complaint.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Administrator'])
def ticket_page(request):
    compliant = UserComplaints.objects.all()
    context = {'compliant': compliant,
               'pageType': 'ticket'}
    return render(request, 'accounts/tickets_page.html', context)


@login_required(login_url='login')
def toggle_true_false(request):
    print(request.GET.get('obj_id'))
    obj = get_object_or_404(UserComplaints, pk=request.GET.get('obj_id'))
    obj.open_close = not obj.open_close
    obj.save()
    return redirect(to='tickets')
