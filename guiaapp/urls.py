from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guiaapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^menu/$', 'guia.views.menu_index'),
    (r'^menu/create/$', 'guia.views.menu_create'),
    (r'^menu/edit/(?P<menu_id>\w+)$', 'guia.views.menu_create'),
    (r'^menu/delete/(?P<menu_id>\w+)$', 'guia.views.menu_delete'),
)
