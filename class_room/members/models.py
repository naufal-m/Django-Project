from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models. DateField(null=True)

    # here the 'Member' is name of the table and firstname nad
    # lastname are the table values.

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
