from django.db import models
from typing import Any

from task_manager.tasks.models import Tasks
from task_manager.tests import TestBase, TestDataBase


# Create your tests here.
class TestTasks(TestDataBase, TestBase):
    model = Tasks
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']
    path_test_data = "test_task.json"
    show_url = 'tasks:tasks_list'
    create_url = 'tasks:create_task'
    edit_url = 'tasks:task_update'
    delete_url = 'tasks:task_delete'

    def assertItem(self, task: models.query.QuerySet[Any], task_data: dict):
        self.assertEqual(task.name, task_data['name'])
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.status.pk, task_data['status'])
        self.assertEqual(task.executor.pk, task_data['executor'])
