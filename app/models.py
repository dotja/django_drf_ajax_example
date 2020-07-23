from django.db import models

# Create your models here.

class Jobs(models.Model):
	JOB_TYPES = [('remote', '1'), ('office', '2')]
	job_type = models.CharField(max_length=10, choices=JOB_TYPES, default='office')
	posted_on = models.DateField()
	location = models.CharField(max_length=50)

