from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'app.views.hora_actual', name='hora_actual'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^plus/(\d+)$', 'app.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'app.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'app.views.categoria', name='categoria'),
    url(r'^add/$', 'app.views.add', name='add'),




    url(r'^admin/', include(admin.site.urls)),
)