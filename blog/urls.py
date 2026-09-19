from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<post_id>', views.delete, name='delete'),
]
