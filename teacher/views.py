from tkinter.messagebox import NO
from unicodedata import name
from rest_framework.views import APIView 
from rest_framework.views import Response
from teacher.models import Teacher
from teacher.serializers import (TeacherSereializer, RegisterTeacherSerializer)
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST)

class TeacherView(APIView):
  def get(self, request, format=None):
    teachers = Teacher.objects.all()
    serializer = TeacherSereializer(teachers, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

  def post(self, request, format=None):
    serializer = RegisterTeacherSerializer(data=request.data)
    if serializer.is_valid():
      teacher = Teacher(
        name = serializer.validated_data.get('name'),
        value = serializer.validated_data.get('value'),
        description = serializer.validated_data.get('description'),
        photo = serializer.validated_data.get('photo')
      )
      teacher.save()
      register_teacher_serializer = RegisterTeacherSerializer(teacher, many=False)
      return Response(register_teacher_serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
