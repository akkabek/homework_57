from curses.ascii import controlnames

from django.views.generic import TemplateView
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

