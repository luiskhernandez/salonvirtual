from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'app.views.home', name='home'),
    # url(r'^salonvirtual/', include('salonvirtual.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login',name="login"),
    url(r'^logout$','app.views.logout_',name="logout"),
    url(r'^dashboard$','app.views.dashboard',name="dashboard"),
    url(r'^admin/', include(admin.site.urls)),
)
