from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('kit/<int:kit_id>/', views.manage_kit, name='manage_kit'),
    path('kit/<int:kit_id>/edit_drug/<int:drug_id>/', views.edit_drug, name='edit_drug'),
    path('kit/<int:kit_id>/take_drug/<int:drug_id>/', views.take_drug, name='take_drug'),
    path('kit/<int:kit_id>/delete_drug/<int:drug_id>/', views.delete_drug, name='delete_drug'),
    path('kit/<int:kit_id>/delete/', views.delete_kit, name='delete_kit'),
    path('delete_usage_history/', views.delete_usage_history, name='delete_usage_history'),

]
