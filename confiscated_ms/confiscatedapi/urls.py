from django.urls import path, include
from .views import ItemAPI,CategoryAPI, DeliveryAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register("items",ItemAPI)
router.register("category",CategoryAPI)
router.register("delivery",DeliveryAPI)

urlpatterns = [
    path('', include(router.urls)),
]
