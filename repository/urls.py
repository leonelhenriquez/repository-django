"""repository URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from allauth.account.views import ConfirmEmailView
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from rest_auth.views import PasswordResetConfirmView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('lista/', include('apps.lista.urls'), name='lista'),
    path('recurso/', include('apps.recurso.urls'), name='recurso'),
    path('rest-auth/', include('apps.usuario.urls'), name='rest-auth'),

    # this url is used to generate email content
    path('passwordreset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
    path('admin/', admin.site.urls),
]