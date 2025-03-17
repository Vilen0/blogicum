from django.urls import include, path

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls')),
    path('posts/<int:id>/', include('blog.urls')),
    path('category/<slug:category_slug>/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

