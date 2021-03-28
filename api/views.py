from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.serializers import CarsSerializers, RateSerializers
from cars.models import Car, RatesNumber


class CarsList(RetrieveUpdateDestroyAPIView):
    serializer_class = CarsSerializers

    def get_queryset(self):
        return Car.objects.all()

    def count_avg(self, rates):
        pass
    #
    # def post(self, ):

# class AddRate(viewsets.ModelViewSet):
#     queryset = RatesNumber.objects.all()
#     serializer_class = RateSerializers
#
#     @action(detail=True, methods=['post'])
#     def enroll(self, request, *args, **kwargs):
#         car_to_rate = self.get_object()
#         car_to_rate.objects.add(request.car)


# class Add(viewsets.ModelViewSet):
# @staticmethod
# def get_url(data):
#     with urlopen(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{data}?format=json') as response:
#         data = response.read()
#         parsed_data = json.loads(data)
#
#         print(parsed_data)
