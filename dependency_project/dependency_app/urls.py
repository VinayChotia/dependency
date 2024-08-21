from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from .models import *
from .views import *

urlpatterns = [
    path('upload/', UploadHarFile.as_view()),
    # # path('export-endpoints/', ExportEndpointsData.as_view(), name='export-endpoints'),
    path('image/',ApiExecutionFlowView.as_view(),name = 'export-png'),
    path('execution/',ExecutionFlow.as_view(),name = 'Execution Flow')
    # path('test/',GetData.as_view()),

]
