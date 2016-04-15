"""wandermap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

import map.views

urlpatterns = [
    url(r'^$', include('map.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/bot', map.views.bot, name='index'),
    url(r'^accounts/login/$', map.views.login, name='index'),
    url(r'^accounts/logout/$', map.views.logout, name='index'),
    url(r'^accounts/loggedin/$', map.views.loggedin, name='index'),
    url(r'^accounts/invalid/$', map.views.invalid_login, name='index'),
    url(r'^accounts/auth/$', map.views.auth_view, name='index'),
	url(r'^accounts/register/$', map.views.register_user, name='index'),
	url(r'^accounts/register_success/$', map.views.register_success, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
