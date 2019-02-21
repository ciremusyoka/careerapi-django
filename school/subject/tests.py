from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class SubjectTests(BaseAPITest):
    def test_creating_subject(self):
        resp=self.create_subject(name="TheSubject")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_subject(self):
        resp=self.client.get(reverse("retrieve_update_destroy_subject",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestSubject")

    def test_updating_subject(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_subject",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")