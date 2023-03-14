from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    name=models.CharField(max_length=100,unique=True)
    address=models.TextField()
    contact_number=models.IntegerField()
    def __str__(self):
        return self.name
















