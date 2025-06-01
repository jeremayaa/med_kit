from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('kit/<int:kit_id>/', views.manage_kit, name='manage_kit'),
    path('kit/<int:kit_id>/edit_drug/<int:drug_id>/', views.edit_drug, name='edit_drug'),
    path('kit/<int:kit_id>/take_drug/<int:drug_id>/', views.take_drug, name='take_drug'),
    path('kit/<int:kit_id>/delete_drug/<int:drug_id>/', views.delete_drug, name='delete_drug'),

]
