from rest_framework import serializers

from school.subject_result.models import SubjectResult


class SubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectResult
        fields="__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=("subject", "result"),
                message=("Result for this subject already added.")
            )
        ]
