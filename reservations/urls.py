from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reservations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^$', 'theatre.views.home', name='home'),
    url(r'^movie/$', 'theatre.views.movie', name='movie'),
    url(r'^get_time/(?P<movieID>\w+)/$', 'theatre.views.get_time', name='get_time'),
    url(r'^api_movie/$', 'theatre.views.api_movie', name='api_movie'),
    url(r'^seat_test/$', 'theatre.views.seat_test', name='seat_test'),
    url(r'^stripe/$', 'theatre.views.stripe', name='stripe'),

)
