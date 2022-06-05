from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.signin,), #name="login"
    #path('home/<str:pk>',views.home),
    path('logout',views.signout,name="logout"),
    path('gdata/',views.gdata),
    #path('home/',views.gdata),
    #path('', views.login),
    path('mycourses/inprogress/', views.mycoursesinprog),
    path('mycourses/completed/', views.mycoursescompleted),
]