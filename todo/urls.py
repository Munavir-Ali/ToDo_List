from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('done/<int:id>/', views.mark_as_done, name='mark_as_done'),
]
