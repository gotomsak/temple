from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
import json
from django.http import Http404, HttpResponse
from .authentication import AccessAuthentication

from rest_framework import permissions
from rest_framework import authentication, permissions, generics


# class GroupViewSet(viewsets.ModelViewSet):
#   queryset = Group.objects.all()
#   serializer_class = GroupSerializer
#
#
# class GenerationGroupViewSet(viewsets.ModelViewSet):
#   queryset = GenerationGroup.objects.all()
#   serializer_class = GenerationGroupSerializer
#
#
# class RegionGroupViewSet(viewsets.ModelViewSet):
#   queryset = RegionGroup.objects.all()
#   serializers_class = RegionGroupSerializer
#
#
# class LandGroupViewSet(viewsets.ModelViewSet):
#   queryset = LandGroup.objects.all()
#   serializers_class = LandGroupSerializer
#
#
# class SpeakerViewSet(viewsets.ModelViewSet):
#   queryset = Speaker.objects.all()
#   serializer_class = SpeakerSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#
#   queryset = User.objects.all()
#   serializer_class = UserSerializer


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

# class Login(APIView):
#   authentication_classes = ()  # 追加
#   permission_classes = ()
#
#   def post(self, request, format=None):
#
#     # リクエストボディのJSONを読み込み、メールアドレス、パスワードを取得
#     try:
#       data = json.loads(request.body)
#       email = data['email']
#       password = data['password']
#     except:
#       # JSONの読み込みに失敗
#       return JsonResponse({'message': 'Post data injustice'}, status=400)
#
#     # メールアドレスからユーザを取得
#     if not User.objects.filter(email=email).exists():
#
#       # 存在しない場合は403を返却
#       return JsonResponse({'message': 'Login failure.'}, status=403)
#
#     user = User.objects.get(email=email)
#
#     # パスワードチェック
#     if not user.check_password(password):
#       # チェックエラー
#       return JsonResponse({'message': 'Login failure.'}, status=403)
#
#     # ログインOKの場合は、トークンを生成
#     token = AccessToken.create(user)
#
#     # トークンを返却
#     return JsonResponse({'token': token.token})


