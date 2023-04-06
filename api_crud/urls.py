
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('v1/', include('inventory.urls')),
    path('auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]