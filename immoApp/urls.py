from . import views
from django.urls import path

app_name = 'immoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:estate_id>/', views.details, name='detail'),
    path('add', views.new_estate, name='new_estate'),
    path('edit/<int:id>/', views.edit_estate, name='edit_estate'),
    path('delete/<int:id>/', views.delete_estate, name='delete_estate')
]