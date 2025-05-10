from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from .models import StudentProfile
from faculty.models import TeacherMaterial, TimeTable, Attendance
from exam.models import Exam
from exam.models import Question, Option, StudentExamResult, StudentExamSummary, Notification
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from django.db import transaction
from datetime import datetime
from collections import defaultdict



def student_login(request):
    if request.method == "POST":
        roll_number = request.POST.get('roll_number')
        password = request.POST.get("password")

        try:
            # try to find user by roll number
            user = CustomUser.objects.get(roll_number=roll_number, user_type='student')

        except CustomUser.DoesNotExist:
            user = None
        

        if user is not None:
            # authentication user
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')
            else:
                return render(request, 'student/student_login.html')
        else:
            return render(request, 'student/student_login.html')
        

    return render(request, 'student/student_login.html')


def user_logout(request):

    logout(request)
    return redirect('login')  # after logout, redirect to login page

