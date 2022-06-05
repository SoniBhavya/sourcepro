from rest_framework import serializers

from .models import login_details
from .models import all_course
from .models import user_courses

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = login_details
        fields = ('email', 'password')


class all_course_serializer(serializers.ModelSerializer):
    class Meta:
        model = all_course
        fields = ('id', 'name', 'total_duration','thumbnail', 'chapters_vls', 'course_description', 'FAQs')


class user_course_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_courses
        fields = ('Course_id','status','deactivation_days_left','course_release_date')