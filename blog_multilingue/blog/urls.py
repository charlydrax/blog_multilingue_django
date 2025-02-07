from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.post_list, name="blog"),
    path('<slug:Slug>/', views.post_detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)