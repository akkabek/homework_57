from django import forms
from django.forms import ModelForm
from issuetracker.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'summary',
            'description',
            'status',
            'type',
        )
        widgets = {
            'summary':     forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status':      forms.Select(attrs={'class': 'form-select'}),
            'type':        forms.Select(attrs={'class': 'form-select'}),
        }