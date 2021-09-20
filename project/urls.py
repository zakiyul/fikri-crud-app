from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add-chef', views.addChef),
    path('edit-chef/<int:pk>', views.editChef),
    path('delete/<int:pk>', views.deleteChef)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
