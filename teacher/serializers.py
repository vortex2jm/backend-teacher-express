from rest_framework import serializers
from teacher.models import Teacher

class TeacherSereializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = "__all__"

class RegisterTeacherSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=255)
  value = serializers.DecimalField(max_digits=10, decimal_places=2)
  description = serializers.CharField()
  photo = serializers.CharField()
