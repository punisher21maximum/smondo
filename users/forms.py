from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Profile_Student, Profile_Teacher


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'phone_number']

class ProfileStudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile_Student
        fields = ['branch', 'academic_year', 'batch', 'roll_no']


class ProfileTeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile_Teacher
        fields = ['branch', 'post_of_teacher']


class ConfirmEmailForm(forms.Form):
    OTP = forms.CharField()

        