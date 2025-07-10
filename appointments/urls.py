from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list, name='appointment-list'),
    path('create/', views.appointment_create, name='appointment-create'),
    path('<int:pk>/', views.appointment_detail, name='appointment-detail'),
    path('<int:pk>/update/', views.appointment_update, name='appointment-update'),
    path('<int:pk>/delete/', views.appointment_delete, name='appointment-delete'),
]
