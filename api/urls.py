from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()
router.register('v1/cars', views.CarsList, basename='cars')

urlpatterns = router.urls

# urlpatterns = [
#     path('v1/cars/', views.CarsList.as_view(), name='cars'),
#
# ]