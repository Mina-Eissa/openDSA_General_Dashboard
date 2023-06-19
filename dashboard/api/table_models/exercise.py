from django.db import models
from .section import Section

class Exercise(models.Model):
    exid = models.AutoField(primary_key=True)
    exname = models.CharField(max_length=100, default='', blank=False)
    number_of_attempts = models.IntegerField(default=0, blank=False)
    number_of_hints = models.IntegerField(default=0, blank=False)
    number_of_incorrect_attempts = models.IntegerField(default=0, blank=False)
    number_of_correct = models.IntegerField(default=0, blank=False)
    secid = models.ForeignKey(Section, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'EXERCISE'
