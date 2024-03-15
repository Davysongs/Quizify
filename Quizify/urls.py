
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RawApp.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
# handler404 = 'RawApp.views.custom_404'
# handler500 = 'RawApp.views.custom_500'