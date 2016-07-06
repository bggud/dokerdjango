from django.db import models
from django.utils import timezone
# Create your models here.
class Docker(models.Model):
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	count_of_containers = models.IntegerField() 
	choose_language = models.CharField(max_length=30)
	code = models.TextField()
	
def __str__(self):
	return self.name
