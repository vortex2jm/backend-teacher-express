from django.db import models

# Create your models here.
class Teacher(models.Model):
  
  name = models.CharField(max_length=100, null=False, blank=False)

  value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

  description= models.TextField(null=False, blank=False)

  photo = models.URLField(null=False, blank=False)
