from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'), # connect members object from views
    path('members/details/<int:id>', views.details, name='details'),
]
