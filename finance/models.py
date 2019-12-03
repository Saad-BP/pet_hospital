from django.db import models
from hospital.models import *
# Create your models here.


class DailyExpenditure(models.Model):
    item = models.CharField(max_length=1000)
    total_unit = models.FloatField(default=1)
    total_cost = models.FloatField()
    date = models.DateField()


YEAR_CHOICES = [
    (2019, "2019"),
    (2020, "2020"),
    (2021, "2021"),
]

MONTH_CHOICES = [(1, 'January'),
                  (2, 'February'),
                  (3, 'March'),
                  (4, 'April'),
                  (5, 'May'),
                  (6, 'June'),
                  (7, 'July'),
                  (8, 'August'),
                  (9, 'September'),
                  (10, 'October'),
                  (11, 'November'),
                  (12, 'December'),
        ]

class ElectricityBill(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES)
    pick_hour_unit = models.FloatField()
    off_pick_hour_unit = models.FloatField()
    total_bill_paid = models.FloatField()
    date_of_payment = models.DateField()


class WasaBill(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES)
    unit = models.FloatField()
    total_bill_paid = models.FloatField()
    date_of_payment = models.DateField()


class CarFuelCost(models.Model):
    item = models.CharField(max_length=1000)
    total_unit = models.FloatField(default=1)
    total_cost = models.FloatField()
    date = models.DateField()


class CylinderBill(models.Model):
    item = models.CharField(max_length=1000)
    total_unit = models.FloatField(default=1)
    total_cost = models.FloatField()
    date = models.DateField()


class UtensilsRecord(models.Model):
    name_of_the_item = models.CharField(max_length=1000)
    number_of_available_items = models.CharField(max_length=1000)
    allocation_area = models.CharField(max_length=1000)
    number_of_wasted_items = models.CharField(max_length=1000)
    note = models.CharField(max_length=1000)
    date = models.DateField()


class SalaryRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="salaries")
    amount = models.FloatField()
    salary_year = models.IntegerField(choices=YEAR_CHOICES)
    salary_month = models.IntegerField(choices=MONTH_CHOICES)
    payment_date = models.DateField()

