from django.views.generic import DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from django.shortcuts import reverse, redirect

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
        return reverse('issuetracker:detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')


class TaskDeleteView(DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('issuetracker:project_detail', kwargs={'pk': self.object.project.pk})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')
