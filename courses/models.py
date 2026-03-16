from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    users_count = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name