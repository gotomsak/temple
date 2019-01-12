from .views import *
from django.urls import path, include



urlpatterns = [
    path('mypage/', AuthInfoGetView.as_view()),

]


