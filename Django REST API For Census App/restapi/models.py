# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.timezone import now


class Admin():
    fname = models.CharField(max_length=60)
    phonenum = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=256)
    betekhnet = models.CharField(max_length=60)
    status = models.CharField(max_length=30, default="valid")
    createdat = models.DateTimeField(default=now, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Datacollectors(models.Model):
    id=models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)
    phonenum = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=256)
    weredabetekhnet = models.CharField(max_length=60)
    status = models.CharField(max_length=30, default="active")
    createdat = models.DateTimeField(default=now, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=30, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'datacollectors'


class Fammember(models.Model):
    #id=models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=60)
    phonenum = models.CharField(max_length=10)
    mname = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    yekrstnasm = models.CharField(max_length=60)
    education = models.CharField(max_length=30)
    bdate = models.IntegerField()
    jobtype=models.CharField(max_length=60)
    parenttype=models.CharField(max_length=60)
    relationtoparent=models.CharField(max_length=60)
    parentid=models.IntegerField(blank=True)
    datacollectorid=models.IntegerField()
    createdat = models.DateTimeField(default=now, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=20,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fammember'


class Kahnat(models.Model):
    title = models.CharField(max_length=60)
    othertitle = models.CharField(max_length=60, blank=True, null=True)
    fname = models.CharField(max_length=60)
    phonenum = models.CharField(max_length=10)
    bdate = models.IntegerField()
    stitle = models.CharField(max_length=60)
    sothertitle = models.CharField(max_length=60, blank=True, null=True)
    sfname = models.CharField(max_length=60, blank=True, null=True)
    jobtype = models.CharField(max_length=60)
    education = models.CharField(max_length=60)
    region = models.CharField(max_length=60)
    zone = models.CharField(max_length=60)
    wereda = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    subcity = models.CharField(max_length=60)
    weredabetekhnet = models.CharField(max_length=60)
    atbiya = models.CharField(max_length=60)
    yemiyageleglubetdebr = models.CharField(max_length=60)
    sebekagubayeabal = models.CharField(max_length=60)
    mothertongue = models.CharField(max_length=60)
    economystatus = models.CharField(max_length=60)
    familynum = models.IntegerField()
    malenum = models.IntegerField()
    femalenum = models.IntegerField()
    plus18num = models.IntegerField()  # Field name made lowercase.
    yenshaljochnum = models.IntegerField(blank=True, null=True)
    housetype = models.CharField(max_length=60)
    datacollectorid = models.ForeignKey(Datacollectors, models.DO_NOTHING, db_column='datacollectorid', blank=True, null=True)
    createdat = models.DateTimeField(default=now, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    updatedby = models.CharField(max_length=20, blank=True, null=True)
    updaterid = models.IntegerField(blank=True, null=True)
    updatedbyfname = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kahnat'


class Memenan(models.Model):
    title = models.CharField(max_length=60)
    othertitle = models.CharField(max_length=60, blank=True, null=True)
    fname = models.CharField(max_length=60)
    gender = models.CharField(max_length=10)
    phonenum = models.CharField(max_length=10)
    bdate = models.IntegerField()
    stitle = models.CharField(max_length=60)
    sothertitle = models.CharField(max_length=60, blank=True, null=True)
    sfname = models.CharField(max_length=60, blank=True, null=True)
    jobtype = models.CharField(max_length=60)
    education = models.CharField(max_length=60)
    region = models.CharField(max_length=60)
    zone = models.CharField(max_length=60)
    wereda = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    subcity = models.CharField(max_length=60)
    weredabetekhnet = models.CharField(max_length=60)
    atbiya = models.CharField(max_length=60)
    atbiyayegebubetzemen = models.CharField(max_length=60)
    yekrstnasm = models.CharField(max_length=60)
    sebekagubayeabal = models.CharField(max_length=60)
    mothertongue = models.CharField(max_length=60)
    economystatus = models.CharField(max_length=60)
    familynum = models.IntegerField()
    malenum = models.IntegerField()
    femalenum = models.IntegerField()
    plus18num = models.IntegerField()
    housetype = models.CharField(max_length=60)
    datacollectorid = models.ForeignKey(Datacollectors, models.DO_NOTHING, db_column='datacollectorid', blank=True, null=True)
    updatedby = models.CharField(max_length=20, blank=True, null=True)
    updaterid = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(default=now, blank=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    updatedbyfname = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memenan'
