# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class ProfessionTests(BaseAPITest):
    def test_creating_profession(self):
        resp=self.create_profession(name="TheProfession")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)

    def test_retrieving_profession(self):
        resp=self.client.get(reverse("retrieve_update_destroy_profession",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestProfession")

    def test_updating_profession(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_profession",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")