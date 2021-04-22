from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ClubViewset

router = routers.DefaultRouter()
router.register('clubs', ClubViewset)

urlpatterns = [
    path('', include(router.urls))
]
