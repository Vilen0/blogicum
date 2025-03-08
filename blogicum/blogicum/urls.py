# blogicum/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from blog import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="blog/index.html"), name='index'),

    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    path('blog/', include('blog.urls', namespace='blog')),
]
