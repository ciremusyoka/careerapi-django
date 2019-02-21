# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class CourseCutoffTests(BaseAPITest):
    def test_creating_course_cutoff(self):
        resp=self.create_course_cutoff(year=2201)
        # print(resp)
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_course_cutoff(self):
        resp=self.client.get(reverse("retrieve_update_destroy_course_cutoff",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["year"], 2001)

    def test_updating_course_cutoff(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_course_cutoff",kwargs={"pk":1}),data={"year":2002})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["year"], 2002)