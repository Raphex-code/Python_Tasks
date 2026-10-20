from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

@login_required
def home(request):
    total_students = Student.objects.count()

    return render(request, 'main_app/home.html', {
        "total_students": total_students,
    })

@login_required
def students(request):
    if request.method == "POST"
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("students")
        else:
            form = StudentForm()

        students = Student.objects.all()

        return render(request, "main_app/student_list.html", {
            "students": students,
            "form": form,
            "show_modal": request.method == "POST"
        })

    return render(request, 'main_app/student_list.html', {
        'students': students
    })

@login_required
def about(request):
    return render(request, 'main_app/about.html')