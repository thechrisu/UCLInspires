from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User) #Connection to base user, defined by Django
    profile_picture = models.CharField(max_length=500)
    gender = models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    type = models.CharField(max_length=100) # School or Uni

    def get_name(self):
        return self.user.first_name

    def get_year_of_study(self):
        return self.year_of_study

    def get_course(self):
        return self.department

    def get_photo(self):
        return self.profile_picture

    def __unicode__(self):          # __unicode__ on Python 2
        return self.user.first_name

User.profile = property(lambda u: UserProfile.objects.get_or_crate(user=u)[0])

class SchoolStudent(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    interests = models.TextField()

    def __unicode__(self):
        return self.user_profile.user.first_name

    def get_name(self):
        return self.user_profile.user.first_name

class UniversityStudent(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    year_of_study = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user_profile.user.first_name

    def get_name(self):
        return self.user_profile.user.first_name

class StudentFollowsUniStudent(models.Model):
    school_student = models.ForeignKey(SchoolStudent)
    uni_student = models.ForeignKey(UniversityStudent, related_name="following")

    def __unicode__(self):
        return "" + self.school_student.user_profile.user.first_name + " is following " + self.uni_student.user_profile.user.first_name






