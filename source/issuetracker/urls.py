from django.urls import path
from issuetracker.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    ProjectDeleteView
from issuetracker.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, TaskCreateInProjectView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('tasks/', TaskListView.as_view(), name='list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='detail'),
    path('tasks/create', TaskCreateView.as_view(), name='create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),
    path('projects/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),

    path('projects/<int:project_pk>/tasks/create/', TaskCreateInProjectView.as_view(), name='task_create_in_project'),

]