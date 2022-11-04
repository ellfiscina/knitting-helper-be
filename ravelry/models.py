from email.policy import default
from django.db import models
from .enums import FiberTypes, AvailableAt


class Company(models.Model):
    name = models.CharField(max_length=200)
    linde_hobby = models.BooleanField(default=False)
    hobbii = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "companies"


class Yarn(models.Model):
    name = models.CharField(max_length=200)
    weight = models.CharField(max_length=200, null=True)
    texture = models.CharField(max_length=200, null=True)
    grams = models.IntegerField(default=0, null=True)
    yardage = models.IntegerField(default=0, null=True)
    min_gauge = models.IntegerField(default=0, null=True)
    max_gauge = models.IntegerField(default=0, null=True)
    gauge_divisor = models.IntegerField(default=0, null=True)
    ravelry_id = models.IntegerField(default=0)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def get_gauge(self):
        if self.max_gauge and self.max_gauge != self.min_gauge:
            max = f' - {self.max_gauge}'
        else:
            max = ''
        return f'{self.min_gauge}{max} / {self.gauge_divisor}'


class Fiber(models.Model):
    name = models.CharField(max_length=200)
    yarns = models.ManyToManyField(Yarn)
    kind = models.IntegerField(
        choices=[(tag, tag.value) for tag in FiberTypes])


ThroughModel = Fiber.yarns.through
