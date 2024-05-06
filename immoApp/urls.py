from . import views
from django.urls import path

app_name = 'immoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:estate_id>/', views.details, name='detail'),
]