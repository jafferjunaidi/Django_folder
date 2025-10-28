"""
URL configuration for Static_dynamic_links project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Static_dynamic_links import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home)  # static URL
    # path('home/<int:sid>',views.home) # dynamic URL with integer parameter
    # path('home/<str:sid>',views.home) # dynamic URL with string parameter
    path('home/<sid>',views.home) # dynamic URL with parameter accepting any string and integer
    # path('about/', views.about),  # static URL
]
