from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from django.shortcuts import get_object_or_404, redirect, reverse

class TaskListView(TemplateView):
    template_name = 'tasks/task_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = Task.objects.all()

        return context

class TaskCreateView(FormView):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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
