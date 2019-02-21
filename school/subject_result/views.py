from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from school.subject_result.models import SubjectResult
from school.subject_result.serializers import SubjectResultSerializer


class ListCreateSubjectResultsAPIView(generics.ListCreateAPIView):
    serializer_class = SubjectResultSerializer
    queryset = SubjectResult.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroySubjectResultAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectResultSerializer
    queryset = SubjectResult.objects.all()



