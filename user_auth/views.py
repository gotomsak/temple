from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from .serializers import *
import json
from django.http import Http404
from .authentication import AccessAuthentication
from rest_framework import permissions



class PositionViewSet(viewsets.ModelViewSet):
  queryset = Position.objects.all()
  serializer_class = PositionSerializer


class BelongViewSet(viewsets.ModelViewSet):
  queryset = Belong.objects.all()
  serializer_class = BelongSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
  queryset = Speaker.objects.all()
  serializer_class = SpeakerSerializer


class UserViewSet(viewsets.ModelViewSet):

  queryset = User.objects.all()
  serializer_class = UserSerializer

class Login(APIView):
  authentication_classes = ()  # 追加
  permission_classes = ()

  def post(self, request, format=None):

    # リクエストボディのJSONを読み込み、メールアドレス、パスワードを取得
    try:
      data = json.loads(request.body)
      email = data['email']
      password = data['password']
    except:
      # JSONの読み込みに失敗
      return JsonResponse({'message': 'Post data injustice'}, status=400)

    # メールアドレスからユーザを取得
    if not User.objects.filter(email=email).exists():

      # 存在しない場合は403を返却
      return JsonResponse({'message': 'Login failure.'}, status=403)

    user = User.objects.get(email=email)

    # パスワードチェック
    if not user.check_password(password):
      # チェックエラー
      return JsonResponse({'message': 'Login failure.'}, status=403)

    # ログインOKの場合は、トークンを生成
    token = AccessToken.create(user)

    # トークンを返却
    return JsonResponse({'token': token.token})


class YesMan(APIView):  # YesManクラスを追加
  authentication_classes = (AccessAuthentication,)  # 追加
  permission_classes = (IsAuthenticated,)
  def post(self, request, format=None):
    return JsonResponse({'message': 'Yes'})
