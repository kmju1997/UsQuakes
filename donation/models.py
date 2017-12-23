# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_pw = models.CharField(max_length=20)
    customer_mail = models.CharField(max_length=100)
    customer_total_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customers'


class Earthquakes(models.Model):
    eq_id = models.AutoField(primary_key=True)
    eq_name = models.CharField(max_length=50)
    eq_region = models.CharField(max_length=30)
    fund_total_amount = models.IntegerField(blank=True, null=True)
    fund_people_num = models.IntegerField(blank=True, null=True)
    start_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earthquakes'


class Fund(models.Model):
    fund_id = models.AutoField(primary_key=True)
    eq = models.ForeignKey(Earthquakes, models.DO_NOTHING)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    fund_amount = models.IntegerField()
    fund_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund'


class Reward(models.Model):
    reward_id = models.AutoField(primary_key=True)
    reward_name = models.CharField(max_length=100)
    reward_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reward'
