from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reservations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^home/$', 'theatre.views.home', name='home'),
    url(r'^profile/$', 'theatre.views.profile', name='profile'),


)
