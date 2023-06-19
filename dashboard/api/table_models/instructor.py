from django.db import models

class Instructor(models.Model):
    instid = models.AutoField(primary_key=True)
    ifirst_name = models.CharField(max_length=50)
    ilast_name = models.CharField(max_length=50)
    iphone_number = models.CharField(max_length=20)
    iemail = models.CharField(max_length=255)
    icountry = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'INSTRUCTOR'
