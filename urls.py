from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('studentregister',views.studentregister,name="studentregister"),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('staffregister',views.staffregister,name="staffregister"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('studentlogout',views.studentlogout,name="studentlogout"),
    path('stafflogout',views.stafflogout,name="stafflogout"),
]
