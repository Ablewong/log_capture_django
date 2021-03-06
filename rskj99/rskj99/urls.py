"""rskj99 URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from logs.views	import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
    (r'^logs/$',list_log),
    (r'^tealogs/$',tea_log),
    (r'loglist/(?P<logs_name>[A-Za-z0-9_-]+.(log|jpg|png|zip)(.\d{4}-\d{2}-\d{2})?)/$',download_log),
    (r'tealog/(?P<tealogs_name>[A-Za-z0-9_-]+.(log|jpg|png|zip)(.\d{4}-\d{2}-\d{2})?)/$',down_tealog),
)
