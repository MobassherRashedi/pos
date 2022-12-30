from django.urls import path
from .views import LoginView
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', LoginView.as_view(), name='accounts.login'),
    path('logout/', LogoutView.as_view(next_page='accounts.login'), name='accounts.logout'),
]
