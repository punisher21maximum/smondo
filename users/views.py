from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm, 
    UserUpdateForm, 
    ProfileUpdateForm, 
    ProfileStudentUpdateForm,
    ProfileTeacherUpdateForm,
    ConfirmEmailForm#reg
)
from django.core.mail import EmailMessage
from django.core.mail import send_mail

def test_email():
    subject = 'Testing email'
    message = "how are you man"
    from_e = "beyond21max@gmail.com"
    to_email = "vishal7x7@gmail.com"
    send_mail(subject, message, from_e, [to_email])

#generate otp
import random
OTP = ''


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('confirm_email')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#register
def confirm_email(request):
    form = ConfirmEmailForm()
    return render(request, 'users/confirm_email.html', {'form': form})

@login_required
def profile(request):
    test_email() ; print("email_sent")
    flag = 's'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if request.user.email.endswith('@mitaoe.ac.in'):
            p_s_form = ProfileStudentUpdateForm(request.POST,
                                       instance=request.user.profile_student)
            if p_s_form.is_valid(): p_s_form.save()
        else :
            flag = 't'
            p_t_form = ProfileTeacherUpdateForm(request.POST,
                                       instance=request.user.profile_teacher)
            if p_t_form.is_valid(): p_t_form.save()

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        if request.user.email.endswith('@mitaoe.ac.in'):
            p_s_form = ProfileStudentUpdateForm(instance=request.user.profile_student)
        else:
            flag = 't'
            p_t_form = ProfileTeacherUpdateForm(instance=request.user.profile_teacher)


    p_x_form = p_s_form if flag=='s' else p_t_form

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_x_form': p_x_form
    }

    return render(request, 'users/profile.html', context)

