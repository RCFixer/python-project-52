from django.db import models

# Create your models here.


class Labels(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
