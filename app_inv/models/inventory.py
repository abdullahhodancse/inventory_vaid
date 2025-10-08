from django.db import models
from django.contrib.auth import get_user_model
from app_inv.models.catagory import Catagory

User = get_user_model()

class inventory(models.Model):

    PRIORITY_CHOICES=[
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=PRIORITY_CHOICES)
    date = models.DateField(auto_now=True)
    catagory = models.ManyToManyField(Catagory,null=True, blank=True)
    number_of_list = models.PositiveBigIntegerField(default=1)


    def __str__(self):
        return f"{self.name} ({self.priority})"



