from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class ResultTests(BaseAPITest):

    def test_creating_result(self):
        resp=self.create_result()
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_result(self):
        resp=self.client.get(reverse("retrieve_update_destroy_result",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["avg_grade"], "E")

    def test_updating_result(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_result",kwargs={"pk":1}),data={"avg_grade":"F"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["avg_grade"], "F")


    def test_creating_one_subject_result_per_result(self):
        resp=self.create_result_subject_results()
        self.assertEquals(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_creating_result_subject_results(self):
        resp=self.create_result_subject_results(subject=2)
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)
        self.assertEquals(resp.data["grade"], "C+")

    def test_listing_result_subjects(self):
        self.test_creating_result_subject_results()
        resp=self.client.get(reverse("list_create_result_subject_results",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["count"], 2)





