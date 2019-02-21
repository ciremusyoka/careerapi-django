from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class SubjectResultTests(BaseAPITest):
    def test_creating_subject_result(self):
        resp=self.create_subject_result(grade="B",subject=2)
        # print(resp)
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_subject_result(self):
        resp=self.client.get(reverse("retrieve_update_destroy_subject_result",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["grade"], "A+")

    def test_updating_subject_result(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_subject_result",kwargs={"pk":1}),data={"points":77})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["points"], 77)