from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student


@login_required
def home(request):
    total_students = Student.objects.count()

    return render(request, 'main_app/home.html', {
        "total_students": total_students,
    })

@login_required
def students(request):
    students = Student.objects.all()

    return render(request, 'main_app/student_list.html', {
        'students': students
    })

@login_required
def about(request):
    return render(request, 'main_app/about.html')