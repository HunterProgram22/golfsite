"""golfsite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rounds.views import home, manage, round_new, \
                        course_new, show, handicap, delete_round, shots_new, \
                        sop


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^manage/$', manage, name='manage'),
    url(r'^round/new/$', round_new, name='round_new'),
    url(r'^course/new/$', course_new, name='course_new'),
    url(r'^shots/new/$', shots_new, name='shots_new'),
    url(r'^show/$', show, name='show'),
    url(r'^delete_round/', delete_round, name='delete_round'),
    url(r'^handicap/$', handicap, name='handicap'),
    url(r'^sop/$', sop, name='sop'),
    url(r'^', home, name='home'),
]
