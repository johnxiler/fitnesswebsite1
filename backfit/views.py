from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admindash')
        # messages.info(request, 'Account not found)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username=username, password=password)
            if user_obj and user_obj.check(is_superuser=True):
                login(request, user_obj)
                return redirect('')
            messages.info(request, 'Invalid password')
            return redirect('admindash')
        return render(request, "admin_login.html")
    except Exception as e:
        print(e)


def admindash(request):
    return render(request, "admindash.html")
