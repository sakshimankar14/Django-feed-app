from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication URLs (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Your feeds app URLs
    path('feeds/', include('feeds.urls')),
    
    # Redirect root URL to feeds
    path('', RedirectView.as_view(url='/feeds/', permanent=True)),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)