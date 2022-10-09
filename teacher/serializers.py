from rest_framework import serializers
from teacher.models import Teacher

class TeacherSereializer(serializers.ModelSerializer):
  class Meta:
    teacher = Teacher()
    fields = '__all__'
