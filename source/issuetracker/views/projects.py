from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from issuetracker.forms import TaskForm
from issuetracker.models import Project
from django.shortcuts import get_object_or_404, redirect

class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.task_set.all()
        return context