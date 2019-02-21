# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class CourseTests(BaseAPITest):
    def test_creating_course(self):
        resp=self.create_course(name="TheCourse")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_course(self):
        resp=self.client.get(reverse("retrieve_update_destroy_course",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestCourse")

    def test_updating_course(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_course",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")

    def test_listing_corses_cutoffs(self):
        resp=self.client.get(reverse("list_create_courses_cutoffs",kwargs={"pk":1}))
        # print(resp)
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["count"], 1)

