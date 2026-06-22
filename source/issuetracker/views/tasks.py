from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from django.shortcuts import get_object_or_404, redirect, reverse

class TaskDetailView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    template_name = 'tasks/task_update.html'
    model = Task
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('projects_detail', kwargs={'pk': self.object.project.pk})
