from django.contrib import admin
from django.urls import path
from teacher.views import TeacherView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers', TeacherView.as_view())
]
