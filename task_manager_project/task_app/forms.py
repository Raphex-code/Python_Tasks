from django import forms
from .models import Task


class TaskForm(from .ModelFrom):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title...', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter task detials...', 'rows': 3, 'class': 'from-control'}),
        }
