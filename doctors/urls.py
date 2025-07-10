from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    # Web Views
    path('', views.doctor_list, name='doctor-list'),
    path('create/', views.doctor_create, name='doctor-create'),
    path('<int:pk>/', views.doctor_detail, name='doctor-detail'),
    path('<int:pk>/update/', views.doctor_update, name='doctor-update'),
    path('<int:pk>/delete/', views.doctor_delete, name='doctor-delete'),
    path('<int:pk>/availability/', views.doctor_availability, name='doctor-availability'),
]