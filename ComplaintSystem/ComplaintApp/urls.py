from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('logout', LogoutView.as_view(next_page = reverse_lazy('home')), name='logout'),
    path('resident/login', views.login_resident, name='resident_login'),
    path('resident/dashboard', views.resident_dashboard, name='resident_dashboard'),
    path('manager/login', views.login_manager, name = 'manager_login'),
    path('manager/dashboard', views.manager_dashboard, name='manager_dashboard'),
]