from rest_framework import serializers

from cars.models import Car, RatesNumber


class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')


class RateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatesNumber
        fields = ('car_id', 'rates_number')