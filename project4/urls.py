from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_accounting.urls')),
    path('accounting/', include('app_accounting.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.sites.AdminSite.site_header = 'Admin Dashboard'
admin.sites.AdminSite.site_title = 'My Title'
admin.sites.AdminSite.site_index = 'My Index'