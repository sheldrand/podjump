from django.conf.urls import patterns, include, url
from djangosite.views import hello, current_time, hour_ahead, current_dt
from podjump import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^t/$', views.search_form),
	url(r'^time/plus/(\d{1,2})+/$', hour_ahead),
	url(r'^time/$', current_dt),
	url(r'^$', views.search_form),
	url(r'^show/$', views.show_connections)
)