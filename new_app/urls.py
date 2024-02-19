from django.urls import path
from . import views

urlpatterns = [
    path('',views.get),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('apilist/', views.display),
    path('apilist/<int:id>/', views.api_details),

]
