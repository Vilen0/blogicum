from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm

urlpatterns = [
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path(
      'auth/registration/',
      CreateView.as_view(
          template_name='registration/registration_form.html',
          form_class=CustomUserCreationForm,
          success_url=reverse_lazy('blog:index'),
      ),
      name='registration',
    ),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
'''