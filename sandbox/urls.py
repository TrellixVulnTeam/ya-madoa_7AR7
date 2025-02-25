import django
from django.apps import apps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views
from oscar.views import handler403, handler404, handler500

from apps.sitemaps import base_sitemaps

admin.autodiscover()

urlpatterns = [
    # Include admin as convenience. It's unsupported and only included
    # for developers.
    url(r'^admin/', admin.site.urls),

    # i18n URLS need to live outside of i18n_patterns scope of Oscar
    url(r'^i18n/', include(django.conf.urls.i18n)),

    # include a basic sitemap
    url(r'^sitemap\.xml$', views.index,
        {'sitemaps': base_sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap,
        {'sitemaps': base_sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns(
    url(r'^', include(apps.get_app_config('oscar').urls[0])),
)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403, {'exception': Exception()}),
        url(r'^404$', handler404, {'exception': Exception()}),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
