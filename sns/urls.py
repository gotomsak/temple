from rest_framework import routers
from .views import *
from django.urls import path
from .views import Login

urlpatterns = [
    path('login', Login.as_view()),
    path('yesman', YesMan.as_view()),

]

router = routers.DefaultRouter()

router.register(r'belong', BelongViewSet)
router.register(r'position', PositionViewSet)
router.register(r'speaker', SpeakerViewSet)
router.register(r'user', UserViewSet)

