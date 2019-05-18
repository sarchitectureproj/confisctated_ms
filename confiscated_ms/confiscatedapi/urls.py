from django.urls import path, include
from .views import index,ItemAPI,CategoryAPI, DeliveryAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register("items",ItemAPI)
router.register("category",CategoryAPI)
router.register("delivery",DeliveryAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
]
