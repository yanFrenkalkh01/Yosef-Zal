from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Profile, UserEvent, UserComplaints
from django.forms import HiddenInput


class CreateUserForm(UserCreationForm):  # Costume forme for register page
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    profile_number = forms.CharField(max_length=100,
                                     required=True,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'profile_number']


group = Group.objects.get(name='Doctor')
user = group.user_set.all()
CHOISES = tuple([(str(name), str(name)) for name in user])
doctor_choise_name = [
    ("רופה משפחה", "רופה משפחה"),
    ("רופה רקטאלי", "רופה רקטאלי"),
    ("רופה עור", "רופה עור")
]


class GenerateEvent(forms.ModelForm):
    doctor = forms.CharField(widget=forms.Select(choices=CHOISES),
                             required=True)

    doctor_type = forms.CharField(required=True,
                                  widget=forms.Select(choices=doctor_choise_name))

    event_date = forms.DateField(label="Date",
                                 widget=forms.DateInput(attrs={'type': 'date'}))

    event_time = forms.TimeField(label="Time",
                                 widget=forms.TextInput(attrs={'type': 'time'}))

    class Meta:
        model = UserEvent
        fields = ['doctor', 'doctor_type', 'event_date', 'event_time', 'event_name']


class EditEventDescription(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = ['description']


class MakeComplaint(forms.ModelForm):
    complaint = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserComplaints
        fields = ['complaint']


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
