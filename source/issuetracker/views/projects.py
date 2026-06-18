from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from django.shortcuts import get_object_or_404, redirect