from django.urls import path
from issuetracker.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('tasks/', TaskListView.as_view(), name='list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='detail'),
    path('tasks/create', TaskCreateView.as_view(), name='create'),
    path('tasks/update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
]