from django.db import models

class Catagory(models.Model):
    user = models.ForeignKey('app_inv.User', on_delete=models.CASCADE, null=True, blank=True,related_name='catagories_fk')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
