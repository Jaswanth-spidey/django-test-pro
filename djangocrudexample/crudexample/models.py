from django.db import models

# Create your models here.

class UserDetails(models.Model):
    first_name = models.CharField("First Name",max_length=255,blank=True,null=True)

    def __str__(self):
        return self.first_name



