from django.conf.urls import patterns, include, url
from djangoSite.views import hello, current_time

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^t/$', current_time),
)
