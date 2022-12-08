from django.db import models

# Create your models here.

'''
class Patient(models.Model):
    name = models.CharField(max_length=20, null=True)
    id = models.IntegerField(max_length=10, null=True)

    def __str__(self):
        return self.name


class PatientList(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True)
    time = models.TimeField(null=True)
    description = models.CharField(max_length=200, null=True)

'''

