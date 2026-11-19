"""
URL configuration for college_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student_portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home_page'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
    path('add/', views.forms1, name='add_data'),
    path('student_form/', views.Student_form_dj, name='student_form'),  
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logout') 
]
