from django.db import models
from students.models import SStudent
# Create your models here.

class MyCourse(models.Model):

    #id = models.AutoField(primary_key=True)
    s_id  = models.ForeignKey(SStudent, default=1, verbose_name="Student", on_delete=models.SET_DEFAULT)
    course_name  = models.CharField(max_length = 50)
    description  = models.TextField()
    start_date   = models.DateField()


    def __str__(self):
        return self.course_name
