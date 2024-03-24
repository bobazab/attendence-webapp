from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def employee_login(request):

    return render(request, 'employee_login.html')

def adminpage(request):

    return render(request, 'adminpage.html')

@login_required
def apply_leave(request):

    return render(request, 'apply_leave.html')

@login_required
def punch_in(request):

    return redirect('home')

@login_required
def punch_out(request):

    return redirect('home')

@login_required
def admin_attendance(request):

    return render(request, 'attendance/admin_attendance.html')