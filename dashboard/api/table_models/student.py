from django.db import models

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sfirst_name = models.CharField(max_length=50, default='', blank=False)
    slast_name = models.CharField(max_length=50, default='', blank=False)
    sphone_number = models.CharField(max_length=20, default='', blank=False)
    semail = models.CharField(max_length=255, default='', blank=False)
    scountry = models.CharField(max_length=30, default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'STUDENT'
