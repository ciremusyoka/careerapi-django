from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from client.models import MyUser


class BaseAPITest(APITestCase):
    username = "michameiu@gmail.com"
    password = "micha"
    client_id = "iuyutyutuyctua"
    client_secret = "lahkckagkegigciegvjegvjhv"
    speaker = None

    def setUp(self):
        user = MyUser.objects.create(username=self.username)
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.user = user
        self.user.set_password(self.password)
        self.user.save()
        program = {"name": "Adeso"}
        # cl = APIClient()
        # resp = cl.post(reverse("list_create_programmes"), program, format="json")
        # self.assertEquals(resp.status_code, status.HTTP_201_CREATED)
        self.create_school()
        self.create_subject()
        self.create_university()
        self.create_personality()
        self.create_profession()
        self.create_course()
        self.create_course_cutoff()
        self.create_subject(name="Math")
        self.create_result()
        self.create_subject_result()
        self.create_prediction()

    def create_university(self,name="TestUniversity"):
        data={"name":name}
        return self.client.post(reverse("list_create_universitys"), data)


    def create_school(self,name="TestSchool",county="KIS"):
        data={"name":name,"county":county}
        return self.client.post(reverse("list_create_schools"),data)

    def create_subject(self,name="TestSubject"):
        data = {"name": name}
        return self.client.post(reverse("list_create_subjects"), data)

    def create_result(self,year=2001,avg_grade="E",avg_points=99):
        data={"user":1,"year":year,"avg_grade":avg_grade,"avg_points":avg_points}
        return self.client.post(reverse("list_create_results"), data)

    def create_subject_result(self,subject=1,grade="A+",points=99):
        data = {"subject": subject, "result": 1,"grade":grade,"points":points}
        return self.client.post(reverse("list_create_subject_results"), data)

    def create_result_subject_results(self,subject=1,grade="C+",points=90):
        data={"subject":subject, "grade":grade,"points":points}
        return self.client.post(reverse("list_create_result_subject_results",kwargs={"pk":1}), data)

    def create_course(self,university=1,profession=1,name="TestCourse"):
        data={"university":university,"profession":profession,"name":name}
        return self.client.post(reverse("list_create_courses"), data)

    def  create_university_courses(self,profession=1,name="TestCourse1"):
        data = {"profession": profession, "name": name}
        return self.client.post(reverse("list_create_university_courses",kwargs={"pk":1}), data)

    def create_course_cutoff(self,course=1,points=99,year=2001):
        data={"course":course,"points":points,"year":year}
        return self.client.post(reverse("list_create_course_cutoffs"), data)

    def create_profession(self,name="TestProfession"):
        data = {"name": name,}
        return self.client.post(reverse("list_create_professions"), data)


    def create_personality(self,name="TestPersonality"):
        data={"name":name}
        return self.client.post(reverse("list_create_personalitys"), data)


    def create_prediction(self, cluster_points=99, personality=1, course=1, result=1):
        data = {"personality": personality, "course": course, "result": result, "cluster_points": cluster_points}
        return self.client.post(reverse("list_create_predictions"), data)

    def create_media(self):
        pass