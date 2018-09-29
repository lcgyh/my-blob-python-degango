from django.db import models

# Create your models here.
class Articel(models.Model):
    title=models.CharField(max_length=32,default="我是标题")
    content=models.TextField(null=True)
    pub_time=models.DateTimeField(null=True)

    def __str__(self):
        return self.title