from django.shortcuts import render
from .models import Student


def home(request):
    name = {'student_name': 'Raphael'}
    return render(request, 'main_app/home.html', name)

def student_list(request):
    students = Student.objects.all()

    return render(request, 'main_app/student_list.html', {
        'students': students
    })

def about_us(request):
    return render(request, 'main_app/about.html')