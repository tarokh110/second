"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')), # new
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    #But we don’t want to build a dedicated
    #pages app just yet, so we can use the shortcut of importing TemplateView and setting
    #the template_name right in our url pattern.
    path('', TemplateView.as_view(template_name='home.html'), name ='home'),
]
