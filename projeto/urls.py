# myragproject/urls.py
from django.contrib import admin
from django.urls import path, include # Adicione include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rag_api.urls')), # Inclui as URLs do nosso app
]