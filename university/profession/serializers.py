from rest_framework import serializers

from university.models import Profession


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession
        fields="__all__"