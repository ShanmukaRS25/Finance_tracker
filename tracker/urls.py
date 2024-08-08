
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
]
