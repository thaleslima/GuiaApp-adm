from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guiaapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', 'guia.views.local_index'),
    (r'^menu/$', 'guia.views.menu_index'),
    (r'^menu/create/$', 'guia.views.menu_create'),
    (r'^menu/edit/(?P<menu_id>\w+)$', 'guia.views.menu_create'),
    (r'^menu/delete/(?P<menu_id>\w+)$', 'guia.views.menu_delete'),

    (r'^city/$', 'guia.views.city_index'),
    (r'^city/create/$', 'guia.views.city_create'),
    (r'^city/edit/(?P<city_id>\w+)$', 'guia.views.city_create'),
    (r'^city/delete/(?P<city_id>\w+)$', 'guia.views.city_delete'),


    (r'^user/$', 'guia.views.user_index'),
    (r'^user/create/$', 'guia.views.user_create'),
    (r'^user/edit/(?P<user_id>\w+)$', 'guia.views.user_create'),
    (r'^user/delete/(?P<user_id>\w+)$', 'guia.views.user_delete'),

    (r'^local/$', 'guia.views.local_index'),
    (r'^local/create/$', 'guia.views.local_create'),
    (r'^local/edit/(?P<local_id>\w+)$', 'guia.views.local_create'),
    (r'^local/delete/(?P<local_id>\w+)$', 'guia.views.local_delete'),
    (r'^get_locals/$', 'guia.views.get_locals'),

    (r'^login-user/(?P<login>\w+)/(?P<password>\w+)$', 'guia.views.login_user'),

    (r'^get-product/$', 'guia.views.get_products'),

)
