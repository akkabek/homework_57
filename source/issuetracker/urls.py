from django.urls import path
from issuetracker.views import IndexView, DetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view(), name='index'),
    path('tasks/<int:pk>', DetailView.as_view(), name='detail'),
]