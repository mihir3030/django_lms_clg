from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import TeacherProfile, TeacherMaterial, TimeTable, Attendance
from exam.models import Exam, Question, Option, Notification
from student.models import StudentProfile
from django.http import Http404
from django.contrib import messages
from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime, date


# Create your views here.



def teacher_login(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        password = request.POST.get('password')


        try:
            #  Find by teacher id
            user = CustomUser.objects.get(teacher_id=teacher_id, user_type='teacher')
        
        except CustomUser.DoesNotExist:
            user = None

        if user is not None:
            # authenticate user
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("teacher_dashboard")
            else:
                return render(request,"faculty/teacher_login.html")
        else:
            return render(request,"faculty/teacher_login.html")
    return  render(request,"faculty/teacher_login.html")


def teacher_logout(request):

    logout(request)
    return redirect("teacher_login")

