from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
  class meta:
    model = Student
    fields = ["student_id", "name", "email", "age"]

    widgets = {
      "student_id": forms.NumberInput(attrs={
        "placeholder": "Enter Student ID",
      }),
      "name": forms.TextInput(attrs={
        "placeholder": "Enter full name",
      }),
      "email": forms.EmailInput(attrs={
        "placeholder": "Enter email address",
      }),
      "age": forms.NumberInput(attrs={
        "placeholder": "Enter age",
      })
    }