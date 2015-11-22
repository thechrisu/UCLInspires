from django.contrib import admin
from .models import UserProfile, UniversityStudent, SchoolStudent, StudentFollowsUniStudent
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(SchoolStudent)
admin.site.register(UniversityStudent)
admin.site.register(StudentFollowsUniStudent)
