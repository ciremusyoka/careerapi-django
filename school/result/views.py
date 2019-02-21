from rest_framework import generics

from mylib.mygenerics import MyListCreateAPIView, MyDjangoFilterBackend
from school.result.models import Result
from school.result.serializers import ResultSerializer
from school.subject_result.models import SubjectResult
from school.subject_result.serializers import SubjectResultSerializer


class ListCreateResultsAPIView(generics.ListCreateAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
    filter_backends = (MyDjangoFilterBackend,)


class RetrieveUpdateDestroyResultAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ListCreateResultSubjectResultsAPIView(MyListCreateAPIView):
    foreign_key_field="result"
    serializer_class = SubjectResultSerializer
    queryset = SubjectResult.objects.all()
    filter_backends = (MyDjangoFilterBackend,)