from django.db import models

# Create your models here.

class SStudent(models.Model):
    #id         = models.AutoField(primary_key=True)
    advisor    = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    user_name  = models.CharField(max_length=50, blank = False)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length = 50)
    email      = models.EmailField(max_length=70,blank=True)
    s_slug     = models.CharField(max_length=100, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Student"


    def __str__(self):
        return self.user_name
