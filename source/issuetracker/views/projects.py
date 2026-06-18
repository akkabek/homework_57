from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from issuetracker.forms import ProjectForm, TaskCreateForProjectForm
from issuetracker.models import Project
from django.shortcuts import get_object_or_404, redirect, reverse

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

class ProjectCreateView(CreateView):
    template_name = 'projects/project_form.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание проекта'
        return context

class ProjectUpdateView(UpdateView):
    template_name = 'projects/project_form.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('projects_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование проекта'
        return context

class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('projects_list')
    context_object_name = 'project'

class TaskCreateInProjectView(CreateView):
    template_name = 'tasks/task_create_in_project.html'
    form_class = TaskCreateForProjectForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.project = self.project
        task.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects_detail', kwargs={'pk': self.project.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context