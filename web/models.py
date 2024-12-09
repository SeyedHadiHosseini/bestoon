from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}-{}".format(self.date, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}-{}".format(self.date, self.amount)
