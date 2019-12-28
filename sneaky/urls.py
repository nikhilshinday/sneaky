"""sneaky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from sneaky.views import index
from sneaky.views import energy
from sneaky.views import people
from sneaky.views import being
from blog.views import blog
from blog.views import blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blogs),
    path('blog/<int:pk>', blog),
    path('energy/', energy),
    path('people/', people),
    path('being/', being)
]
