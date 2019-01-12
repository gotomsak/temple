from .views import *
from django.urls import path, include



# router = routers.DefaultRouter()
#
# router.register(r'region', RegionGroupViewSet)
# router.register(r'group', GroupViewSet)
# router.register(r'land', LandGroupViewSet)
# router.register(r'generation', GenerationGroupViewSet)
# router.register(r'speaker', SpeakerViewSet)
# router.register(r'user', UserViewSet)

urlpatterns = [
    #path('login', Login.as_view()),
    path('mypage/', AuthInfoGetView.as_view()),

]


