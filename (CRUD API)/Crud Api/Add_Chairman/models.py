from django.db import models

# Create your models here.
class Chairman(models.Model):
    Chairman_Name = models.CharField(max_length=100)
    Chairman_Username=models.EmailField(max_length=100,unique=True)
    Chairman_Password=models.CharField(max_length=100,unique=True)
    Chairman_Department =models.CharField(max_length=100,unique=True)
    Department_Id=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)