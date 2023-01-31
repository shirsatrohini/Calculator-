from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class calculator(models.Model):
    # manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    query=models.CharField(max_length=200)
    ans=models.IntegerField()

    def __str__(self):
        return self.query +"-"+str(self.ans)
