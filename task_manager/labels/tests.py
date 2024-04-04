from django.db import models
from typing import Any

from task_manager.labels.models import Labels
from task_manager.tests import TestBase, TestDataBase


# Create your tests here.
class TestStatuses(TestDataBase, TestBase):
    fixtures = ['labels.json', 'users.json']
    path_test_data = "test_labels.json"
    model = Labels
    show_url = 'labels:labels_list'
    create_url = 'labels:create_label'
    edit_url = 'labels:label_update'
    delete_url = 'labels:label_delete'

    def assertItem(
        self,
        status: models.query.QuerySet[Any],
        status_data: dict
    ) -> None:
        self.assertEqual(status.name, status_data['name'])
