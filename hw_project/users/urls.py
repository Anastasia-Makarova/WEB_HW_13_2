from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm
# from ..hw_project.settings import LOGOUT_REDIRECT_URL


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',
         LoginView.as_view(template_name='users/login.html', form_class=LoginForm, redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='quotes:root'), name='logout')
]