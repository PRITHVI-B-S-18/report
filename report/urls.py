"""
URL configuration for report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mentor_report import views as test_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',test_views.signin,name="login"),
    path('home/',test_views.NameList.as_view(),name="home"),
    path('students/<int:pk>',test_views.StudentsList.as_view(),name="students"),
]
