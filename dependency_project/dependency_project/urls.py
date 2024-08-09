from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dependency_app.urls')),
    

]
