"""
URL configuration for django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from users import views
from django.contrib import admin
# this is for render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # path('', views.getUserRoutes),
    path('', views.home_views, name="home_views"),
    path('admin/', admin.site.urls),

]

# this is for render
urlpatterns += staticfiles_urlpatterns()
