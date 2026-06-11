from django.urls import path
from issuetracker.views import IndexView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('tasks/', IndexView.as_view(), name='list'),
    path('tasks/<int:pk>', DetailView.as_view(), name='detail'),
    path('tasks/create', CreateView.as_view(), name='create'),
    path('tasks/update/<int:pk>', UpdateView.as_view(), name='update'),
    path('tasks/delete/<int:pk>', DeleteView.as_view(), name='delete'),
]