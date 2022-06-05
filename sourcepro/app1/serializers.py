from rest_framework import serializers
from .models import all_courses
from .models import usr_course
from .models import quizes

class all_courses_serializer(serializers.ModelSerializer):
    class Meta:
        model = all_courses
        fields = '__all__'


class usr_course_serializer(serializers.ModelSerializer):
    class Meta:
        model = usr_course
        fields = '__all__'


class quiz_serializer(serializers.ModelSerializer):
    class Meta:
        model = quizes
        fields = ('course_id', 'que_options')