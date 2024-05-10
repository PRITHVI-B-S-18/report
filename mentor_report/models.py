from django.db import models

class mentor_tb(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    m_name = models.CharField(max_length=255)
    m_dept = models.CharField(max_length=255)
    m_batch = models.IntegerField(null=False)
    m_students = models.IntegerField(null=False)

    def __str__(self):
        return self.m_name
    
    
class std_details(models.Model):
    mid = models.IntegerField(null=False)
    s_roll = models.CharField(null=False)
    s_name = models.CharField(max_length=255)
    s_email = models.CharField(max_length=255)
    s_phone = models.IntegerField(null=False)
    
    def __str__(self):
        return self.s_name

