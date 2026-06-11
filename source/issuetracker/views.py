from django.views.generic import TemplateView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from django.shortcuts import get_object_or_404, redirect

class IndexView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = Task.objects.all()

        return context

class DetailView(TemplateView):
    template_name = 'webapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs['pk'])
        return context

class CreateView(TemplateView):
    template_name = 'webapp/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')