from rest_framework.views import APIView 
from rest_framework.views import Response
from teacher.models import Teacher
from teacher.serializers import TeacherSereializer
from rest_framework.status import HTTP_200_OK

class TeacherView(APIView):
  def get(self, request, format=None):
    teachers = Teacher.objects.all()
    serializer = TeacherSereializer(teachers, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
