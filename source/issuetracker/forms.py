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