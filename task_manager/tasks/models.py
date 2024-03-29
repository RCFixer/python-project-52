from django.db import models

from task_manager.users.models import CustomUser
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='author')
    executor = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='executor')
    status = models.ForeignKey(Statuses, on_delete=models.RESTRICT, related_name='status')
    created_at = models.DateTimeField(auto_now=True)
    labels = models.ManyToManyField(Labels)

    def __str__(self):
        return self.name
