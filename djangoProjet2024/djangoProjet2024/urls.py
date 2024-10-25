"""
URL configuration for djangoProjet2024 project.

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
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('conferences/', include('Conference.urls'))  # Conference esm l module= application 
]

if settings.DEBUG:

  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> 61cdb3fe31232fa5ce08776b4aa46d177974e92e
