from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # PYTHON SOCIAL AUTH
    url('', include('social.apps.django_app.urls', namespace='social')),
    

    url(r'', include('apps.users.urls')),
    url(r'', include('apps.restaurants.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
