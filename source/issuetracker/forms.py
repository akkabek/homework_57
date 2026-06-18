from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm
from issuetracker.models import Task, Project

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
            'type':        forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        summary = cleaned_data.get("summary")
        description = cleaned_data.get("description")

        if summary and description and summary == description:
            raise ValidationError("Заголовок и подробное описание не могут быть похожи")
        return cleaned_data

    def clean_summary(self):
        summary = self.cleaned_data['summary']

        if len(summary) < 7:
            raise ValidationError('Заголовок слишком короткий!')

        return summary

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'begin_date', 'end_date')
        widgets = {
            'title':       forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'begin_date':  forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date':    forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }