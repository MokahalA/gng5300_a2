from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import custom_logout

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_details, name='student_details'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]