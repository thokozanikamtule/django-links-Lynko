from django.contrib.auth.models import AbstractUser
from django.db import models

class Plan(models.Model):
	name = models.CharField(max_length=255)
	max_num_links = models.IntegerField()

# Create your models here.
class User(AbstractUser):
	Plan = models.ForeignKey(Plan, related_name='users', default=1, on_delete=models.CASCADE)
	
