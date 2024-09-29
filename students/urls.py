from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:pk>/', views.student_details, name='student_details'),
    path('add/', views.student_create, name='student_create'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
]