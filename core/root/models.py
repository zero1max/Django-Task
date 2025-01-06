from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
