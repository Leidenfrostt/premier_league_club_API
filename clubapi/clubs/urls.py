from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ClubViewSet

router = routers.DefaultRouter()  # create a router
router.register('clubs', ClubViewSet)  # register ClubViewSet

# API URLs determined automatically by the router
urlpatterns = [
    path('', include(router.urls))
]
