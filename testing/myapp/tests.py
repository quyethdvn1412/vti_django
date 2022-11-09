from django.test import TestCase
import inspect

from myapp.models import TODOList
from myapp.utils import send_test_csv_report

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# Create your tests here.

TEST_RESULTS = []

class A_TODOListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='addminpass')
        self.other_user = User.objects.create_user(username='other_user', password='addminpass')
        self.task = TODOList.objects.create(user=self.user, title='My Initial Task')
        self.client = APIClient()

    @classmethod
    def tearDownClass(cls):
        User.objects.filter(username__in=['test_user', 'other_user']).delete()

    def test_create_task_with_un_authenticate_user(self):
        """
        In this Test Case we are testing the TODO Create API using an unauthenticated user.
        """

        response = self.client.post(reverse('todo'), {'title': 'My Task 1'}, format='json')

        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Un-authenticated user cannot add a task into the TODO List"
        })

    def test_get_other_user_task_detail(self):
        """
        In this Test Case we are testing the TODO GET API, and trying to get task details of a user using a different user credentials.
        """

        self.client.login(username='other_user', password='adminpass')

        response = self.client.get(reverse('todo-detail', args=[str(self.task.id)]))
        
        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Only the Owner can view the Task Detail"
        })

    def test_create_task_with_authenticated_user(self):
        self.client.login(username='test_user', password='adminpass')

        response = self.client.post(reverse('todo'), {'title': 'My Task 1'}, format='json')

        is_passed = response.status_code == status.HTTP_201_CREATED

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Task Added into the TODO List Successfully"
        })

    def test_get_task_detail(self):
        self.client.login(username='test_user', password='adminpass')

        response = self.client.get(reverse('todo-detail', args=[str(self.task.id)]))
        
        is_passed = response.status_code == status.HTTP_200_OK

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Task Detail Retrieved Successfully"
        })

class B_CSVReportTest(APITestCase):
    def test_send_csv(self):
        send_test_csv_report(test_results=TEST_RESULTS)