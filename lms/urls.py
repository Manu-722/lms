"""
URL configuration for lms project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from lms.views import landing, home
from . import views
from django.contrib.auth import views as auth_views
from lms import views as lms_views
from users import views as user_views 

urlpatterns = [
    # path('', home),  
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('dashboard/', home, name='home'),
    path('users/', include('users.urls')),
    # path('courses/', include('courses.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register, name='register'),
    path('assignments/', include('assignments.urls')),
    path('communication/', include('communication.urls')),
    path('grades/', include('grades.urls')),
    path('api/', include('api.urls')),
    path('', include(('users.urls', 'users'), namespace='users')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)