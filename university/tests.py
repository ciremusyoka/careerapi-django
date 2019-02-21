# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class UniversityTests(BaseAPITest):
    def test_creating_university(self):
        resp=self.create_university(name="TheUniversity")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_university(self):
        resp=self.client.get(reverse("retrieve_update_destroy_university",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestUniversity")

    def test_updating_university(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_university",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")

    def test_creating_university_courses(self):
        resp=self.create_university_courses()
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)
        self.assertEquals(resp.data["university"], 1)

    def test_listing_university_courses(self):
        self.test_creating_university_courses()
        resp=self.client.get(reverse("list_create_university_courses",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["count"], 2)