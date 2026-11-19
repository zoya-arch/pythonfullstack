from django.db import models

class Student_table(models.Model):
    reg_no=models.IntegerField(),
    name=models.CharField(max_length=20),
    email=models.EmailField(default='example@gmail.com'),
    marks=models.DecimalField(decimal_places=5),
    date=models.DateField()

    def __str__(self):
        return self.name+'-'+self.reg_no

# Create your models here.
