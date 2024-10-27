from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('auth/', include('apps.accounts.urls', namespace='accounts')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
