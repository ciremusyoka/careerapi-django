
from rest_framework import generics

from mylib.mygenerics import MyDjangoFilterBackend
from prediction.personality.models import Personality
from prediction.personality.serializers import PersonalitySerializer


class ListCreatePersonalitys(generics.ListCreateAPIView):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer
    filter_backends = (MyDjangoFilterBackend,)




class RetrieveUpdateDestroyPersonalitys(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer