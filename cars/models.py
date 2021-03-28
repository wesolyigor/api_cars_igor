from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100, null=False, default=None, unique=True)
    model = models.CharField(max_length=100, null=False, unique=False)
    avg_rating = models.FloatField(default=0.0)


class RatesNumber(models.Model):
    RATES_NUMBER = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    car_id = models.ForeignKey("Car", on_delete=models.CASCADE)
    rates_number = models.IntegerField(choices=RATES_NUMBER, default=0, verbose_name='rates_number')




# class Rating(models.Model):
#     car = models.ForeignKey('Car', on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField(default=0, verbose_name='rating')
#
#     def __str__(self):
#         return f"{self.car, self.rating}"
#
#
# class RatesNumber(models.Model):
#     car = models.ForeignKey('Car', on_delete=models.CASCADE)
#     RATES_NUMBER = (
#         ('1', 1),
#         ('2', 2),
#         ('3', 3),
#         ('4', 4),
#         ('5', 5),
#     )
#     rates_number = models.CharField(choices=RATES_NUMBER, default=0, verbose_name='rates_number', max_length=10)
#
#     def __str__(self):
#         return f"{self.car, self.rates_number}"
#
#
# class AvgRating(models.Model):
#     car = models.ForeignKey('Car', on_delete=models.CASCADE)
#     avg_rating = models.DecimalField(default='0.0', max_digits=3, decimal_places=1)
#
#     def __str__(self):
#         return f"{self.car, self.avg_rating}"
#
#
# class Car(models.Model):
#     make = models.CharField(max_length=100, null=False, default=None, unique=True)
#     model = models.CharField(max_length=100, null=False, unique=False)
#
#     # avg_rating = models.ForeignKey('AvgRating', on_delete=models.CASCADE)
#     # rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.make, self.model}"
