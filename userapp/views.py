from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout

from .models import SignUp

import random
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForm


# Create your views here.

def signup(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        password1 = request.POST.get('pass1')

        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.warning(request, "Username already exist try another.")
                return redirect('signup')
        
            user = User.objects.create_user(username=name, email=email, password=password)
            user.set_password(password)
            user.save()
            otp = random.randint(0000, 9999)
            prof = SignUp(user = user, token = otp)
            prof.save()
            subject = 'Your Account Verification OTP'
            message = f' Hi here is your account verification otp : {otp} '
            email_from = settings.EMAIL_HOST_USER
            recipient = [email]
            send_mail(subject, message, email_from, recipient)

            messages.success(request, "Account created, to verify check your mail.")
            return redirect('verify_acco')

        else:
            messages.warning(request, "Your Given Password don't Matched.")
    return render (request, 'user_temp/signup.html')


def signin(request):
    if request.method =="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = name, password = password)
        if user:
            prof = SignUp.objects.get(user = user)
            if prof.is_verified == True:
                login(request, user)
                messages.warning(request, "Successfully signed in.")            
                return redirect('home')
            else:
                messages.warning(request, "Please Verify Your Account.")
                return redirect('login_user')
        else:
            messages.warning(request, "User Not Found.")
    return render (request, 'user_temp/signin.html')


def signout(request):
    logout(request)
    messages.warning(request, "User Signed out Successfully.")
    return redirect ('signin')


def verify_acco(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # print(otp)  [for otp print]
        try:
            prof = SignUp.objects.get(token = otp)
            # print(prof) [for profile print]
            prof.is_verified = True
            prof.save()
            messages.success(request, "Profile Seccessfully verified.")
            return redirect('signin')
        except:
            messages.warning(request, "Wrong OTP.")
            return redirect(verify_acco)
    return render (request, 'user_temp/verify.html')


def change_pass(request):
    if request.method == 'POST':
        changeform = PasswordChangeForm(user=request.user, data = request.POST)
        if changeform.is_valid():
            changeform.save()
        update_session_auth_hash(request,changeform.user)
        messages.success(request, "Password has been changed Seccessfully.")
        return redirect('home')
    else:
        changeform = PasswordChangeForm(user=request.user)
    return render(request,'user_temp/change_password.html', {'changeform' : changeform})