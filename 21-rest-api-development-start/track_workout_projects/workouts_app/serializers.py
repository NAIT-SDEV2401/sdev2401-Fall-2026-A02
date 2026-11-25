# a serializer converts data from its current form into
# a form that can be easily moved between locations/systems

from rest_framework import serializers

from .models import Exercise

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.ChoiceField(choices=Exercise.EXERCISE_TYPES)

    # added create method to handle the logic for creating new Exercise instances
    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)
