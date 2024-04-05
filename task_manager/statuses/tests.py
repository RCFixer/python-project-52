from django.db import models
from typing import Any

from task_manager.statuses.models import Statuses
from task_manager.tests import TestBase, TestDataBase


# Create your tests here.
class TestStatuses(TestDataBase, TestBase):
    fixtures = ['statuses.json', 'users.json']
    path_test_data = "test_status.json"
    model = Statuses
    show_url = 'statuses:statuses_list'
    create_url = 'statuses:create_status'
    edit_url = 'statuses:status_update'
    delete_url = 'statuses:status_delete'

    def assertItem(
        self,
        status: models.query.QuerySet[Any],
        status_data: dict
    ) -> None:
        self.assertEqual(status.name, status_data['name'])
