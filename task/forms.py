from django import forms
from task.models import Task

# Djansgo ModelForm for Task model
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border-2 border-red-500 py-10 w-full', 'placeholder': 'Enter Task Title'}),
            'description': forms.Textarea(attrs={'class': 'border-2 border-red-500 py-10 w-full', 'placeholder': 'Enter Task Description'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'assigned_to': forms.CheckboxSelectMultiple(),
        }