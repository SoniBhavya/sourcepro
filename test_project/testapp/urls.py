from django.urls import path
from . import views

urlpatterns = [
    path('ask_form',views.sample,name="sample_page"),
    path('',views.sample,name="sample_page")
]