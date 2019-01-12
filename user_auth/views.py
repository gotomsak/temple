from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from .serializers import *
from rest_framework import authentication, permissions, generics



class AuthInfoGetView(generics.RetrieveAPIView):
  #permission_classes = (permissions.IsAuthenticated,)
  queryset = Speaker.objects.all()
  serializer_class = SpeakerSerializer

  def get(self, request, format=None):

    return Response(data={
      'username': request.user.username,
      'email': request.user.email,
      #'group': Group.objects.all(),
      #'generation': SpeakerSerializer,

      #'profile': request.user.profile,
    },
      status=status.HTTP_200_OK)

