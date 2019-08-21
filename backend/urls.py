from django.urls import path, include
from django.conf import settings
from django.contrib import admin

import backend.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.vuenote.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', backend.views.index),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
