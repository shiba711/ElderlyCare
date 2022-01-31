from django.db import models
from rest_framework import serializers
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        # return {"name": self.name, "age": self.age}
        # return {"name": self.name}
          return self.name
class Task(models.Model):
    name = models.CharField(max_length=200)
    task_time = models.DateTimeField('task_time')
    done = models.BooleanField(default=False)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name + " " + self.name


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"