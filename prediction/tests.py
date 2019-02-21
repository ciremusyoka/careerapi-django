# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class PredictionTests(BaseAPITest):
    def test_creating_prediction(self):
        resp=self.create_prediction(cluster_points=87)
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_prediction(self):
        resp=self.client.get(reverse("retrieve_update_destroy_prediction",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["cluster_points"], 99)

    def test_updating_prediction(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_prediction",kwargs={"pk":1}),data={"cluster_points":9})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["cluster_points"], 9)