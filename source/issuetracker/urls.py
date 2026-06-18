from django.urls import path
from issuetracker.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from issuetracker.views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('tasks/', TaskListView.as_view(), name='list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='detail'),
    path('tasks/create', TaskCreateView.as_view(), name='create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),

]