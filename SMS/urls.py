"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from enroll import views
from rest_framework.authtoken.views import obtain_auth_token
from enroll.auth import CustomAuthToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/', views.StudentAPI.as_view()),
    path('subjectinfo/', views.SubjectAPI.as_view()),
    path('teacherinfo/', views.TeacherAPI.as_view()),
    path('classinfo/', views.ClassAPI.as_view()),
    # path('gettoken', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
    # path('register/', views.Register.as_view())
]
