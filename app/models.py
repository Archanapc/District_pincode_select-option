from django.db import models


# Create your models here.
class DistrictModel(models.Model):
    did = models.IntegerField(primary_key=True)
    districtname = models.CharField(max_length=200)

    class Meta:
        db_table = "districttable"


class PincodeModel(models.Model):
    pinid = models.IntegerField(primary_key=True)
    pincodeno = models.CharField(max_length=200)
    did = models.IntegerField()

    class Meta:
        db_table = "pintable"

class Person(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)

    class Meta:
        db_table = "app_person"


