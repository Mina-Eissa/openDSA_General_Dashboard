from django.db import models
from .chapter import Chapter

class Section(models.Model):
    secid = models.AutoField(primary_key=True)
    secname = models.CharField(max_length=100, default='', blank=False)
    number_of_exercises = models.IntegerField(default=0, blank=False)
    chid = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'SECTION'
