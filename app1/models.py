from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    comments=models.TextField(max_length=3000)

    def __str__(self):
        return self.name

class service(models.Model):
    name=models.CharField(max_length=100)
    discription=models.CharField(max_length=200)
    amount=models.IntegerField()
    duration=models.IntegerField()
    def __str__(self):
        return self.name
class orderdetails(models.Model):
    id=models.AutoField(unique=True,primary_key=True)
    name=models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
    email=models.EmailField(max_length=200)
    type_of_service=models.CharField(max_length=500)
    paid_method=models.CharField(max_length=500)
    vechile_type=models.CharField(max_length=500,null=True)
    order_placed_time=models.DateTimeField(null=True)
    booked_slot=models.DateField(null=True)
    percentage_of_work_complete=models.IntegerField(null=True)
    sent_mail=models.BooleanField(default=False,help_text="Don't change the field.if mail sent to user then automatically changed that field.when you go to home page ")

    def __str__(self):
        per=str(self.percentage_of_work_complete)
        na=str(self.name)
        if per=="100" and self.sent_mail:
                       return na+" (completed)"
        else:
            return na+" (pending.....)"

