from django.db import models


class catagory(models.Model):
   
    name=models.CharField(max_length=200,)


    def __str__(self):
        return self.name