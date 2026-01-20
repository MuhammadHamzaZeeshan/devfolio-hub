from django.contrib import admin
from django.urls import include, path
from django.contrib import admin

admin.site.site_header = "DevFolio Hub Administration"
admin.site.site_title = "DevFolio Admin Portal"
admin.site.index_title = "Welcome to your Portfolio Manager"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('resume/', include('apps.resume.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
]
