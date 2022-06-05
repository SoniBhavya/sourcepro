from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('mycourses/', views.mycourses),
    path('in_course/<str:pk>/', views.in_course),
    path('in_course/<str:pk>/quiz/', views.quiz),
]