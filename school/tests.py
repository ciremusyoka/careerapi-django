# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class SchoolTests(BaseAPITest):
    def test_creating_school(self):
        resp=self.create_school(name="TheSchool")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_school(self):
        resp=self.client.get(reverse("retrieve_update_destroy_school",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestSchool")

    def test_updating_school(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_school",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")

