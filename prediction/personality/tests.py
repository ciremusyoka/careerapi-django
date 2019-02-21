from rest_framework import status
from rest_framework.reverse import reverse

from mylib.tests import BaseAPITest


class PersonalityTests(BaseAPITest):
    def test_creating_personality(self):
        resp=self.create_personality(name="ThePersonality")
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)


    def test_retrieving_personality(self):
        resp=self.client.get(reverse("retrieve_update_destroy_personality",kwargs={"pk":1}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "TestPersonality")

    def test_updating_personality(self):
        resp=self.client.patch(reverse("retrieve_update_destroy_personality",kwargs={"pk":1}),data={"name":"Hello"})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertEquals(resp.data["name"], "Hello")