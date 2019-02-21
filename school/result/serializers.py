from rest_framework import serializers

from school.result.models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields="__all__"


