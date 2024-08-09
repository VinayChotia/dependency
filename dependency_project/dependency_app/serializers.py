from rest_framework import serializers
from .models import *

class FileUploadSerializer(serializers.ModelSerializer):
    # initialize fields
    # files = serializers.FileField()

    class Meta:
        model = HarFile
        fields = '__all__'


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoints
        fields = '__all__'