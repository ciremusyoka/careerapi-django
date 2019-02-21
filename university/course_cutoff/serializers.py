from rest_framework import serializers

from university.models import CourseCutoff


class CourseCutoffSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCutoff
        fields="__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=("year", "course"),
                message=("Cuttoff points for this course and year already added.")
            )
        ]