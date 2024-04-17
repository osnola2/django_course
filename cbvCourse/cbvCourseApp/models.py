from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=21)
    description = models.CharField(max_length=210)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name + self.name + self.score
