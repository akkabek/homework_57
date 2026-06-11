from django.urls import path
from issuetracker.views import IndexView, DetailView, CreateView

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('tasks/', IndexView.as_view(), name='list'),
    path('tasks/<int:pk>', DetailView.as_view(), name='detail'),
    path('tasks/create', CreateView.as_view(), name='create'),
]