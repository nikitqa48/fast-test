from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..user_code import qs
from .models import Model


class TestCoursesAPI(APITestCase):
    def test_get_course_detail_not_auth(self):

        queryset = Model.objects.all()
        self.assertEqual(qs, queryset)

