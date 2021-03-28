from django.shortcuts import render

# Create your views here.
# from django.views.generic import ListView
#
# from cars.models import Car
#
#
# class ListCarsViews(ListView):
#     model = Car
#     context_object_name = 'cars'
#
#     def get_queryset(self):
#         data = self.request.GET.get('s')
#         if data:
#             url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{self.request.data["make"].upper()}?format=json'
