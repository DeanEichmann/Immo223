from . import views
from django.urls import path

app_name = 'immoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Estate_id>/', views.details, name='detail'),
    path('add', views.new_Estate, name='new_Estate'),
    path('edit/<int:id>/', views.edit_Estate, name='edit_Estate'),
    path('delete/<int:id>/', views.delete_Estate, name='delete_Estate')
]