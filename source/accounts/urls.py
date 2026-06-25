from django.urls import path
from django.contrib.auth.views import LoginView

from accounts.views import logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]