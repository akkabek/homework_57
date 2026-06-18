from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from issuetracker.forms import TaskForm
from issuetracker.models import Project
from django.shortcuts import get_object_or_404, redirect

class ProjectListView(ListView):
    template_name =
