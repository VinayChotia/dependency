from django.db import models

class HarFile(models.Model):
    file_upload = models.FileField(upload_to='har_file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Endpoints(models.Model):
    base_path = models.CharField(max_length=100,blank = True,null=True)
    path = models.CharField(max_length=100)
    
    query_params = models.CharField(max_length=100,blank = True,null=True)
    method = models.CharField(max_length=10)
    requestBody = models.TextField(blank=True,null=True)
    headers = models.TextField(blank=True,null=True)
    referrer = models.TextField(blank = True)
    request_parameters = models.JSONField (blank=True)
    response_parameters = models.JSONField (blank=True)
    responses = models.TextField(blank=True)
    is_producer_api = models.BooleanField(default=False)
    response_header = models.TextField(blank = True)
    responsebody = models.TextField(blank=True)
    authentication = models.TextField(blank=True,null=True)
    dependency_list = models.TextField(blank=True,null=True)
    # dependencies = models.ManyToManyField('self', blank=True,)
    

    def __str__(self):
        return f"{self.method} {self.base_path} {self.path} {self.query_params}"
