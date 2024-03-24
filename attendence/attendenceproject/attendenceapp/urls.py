from django.urls import path
from . import views
app_name='attendenceapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.adminpage, name='adminpage'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('punch_in/', views.punch_in, name='punch_in'),
    path('punch_out/', views.punch_out, name='punch_out'),
    path('admin/attendance/', views.admin_attendance, name='admin_attendance'),
]

