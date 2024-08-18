from django.db import models


class project(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to= 'project_images/', blank=True)