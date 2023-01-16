from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('', include('django_social_share.urls', namespace='social')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)