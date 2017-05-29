"""tema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from orar import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^my_events/$', views.view_my_events),
    url(r'^parse/$', views.parser),

    url(r'^$', views.all_group_events),
    url(r'^add_event/(?P<event_id>\d+)/$', views.add_event_to_user),
    url(r'^remove_event/(?P<event_id>\d+)/$', views.remove_event_from_user),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^login/', auth_views.login, name='login'),
]
