from django.db import models
from django.utils import timezone
import hashlib
from datetime import timedelta

from django.contrib.auth.models import *

# Create your models here.


# 部を入れるテーブル
class GenerationGroup(models.Model):
  generation_text = models.CharField(max_length=50, unique=True)


# 地域
class RegionGroup(models.Model):
  region_text = models.CharField(max_length=50, unique=True)


# 班
class LandGroup(models.Model):
  land_text = models.CharField(max_length=50, unique=True)


# 講員をUserに追加
class Speaker(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image_path = models.ImageField(max_length=100)
  notice_auth = models.BooleanField(default=False)
  generation = models.ForeignKey(GenerationGroup, on_delete=models.CASCADE)

  # lineノアレみたいな
  status_message = models.CharField(max_length=100)
  # 地域名
  region = models.ForeignKey(RegionGroup, on_delete=models.CASCADE)
  # 支部名
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  # 班
  land = models.ForeignKey(LandGroup, on_delete=models.CASCADE)


# AccessTokenのテーブル
# class AccessToken(models.Model):
#
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   token = models.CharField(max_length=40)
#   access_datetime = models.DateTimeField()
#
#   def __str__(self):
#     # メールアドレスとアクセス日時、トークンが見えるようにする
#     dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
#     return self.user.email + '(' + dt + ') - ' + self.token
#
#
#   @staticmethod
#   def create(user: User):
#     # ユーザの既存のトークンを取得
#     if AccessToken.objects.filter(user=user).exists():
#       # トークンが既に存在している場合は削除する
#       AccessToken.objects.get(user=user).delete()
#
#     # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
#     dt = timezone.now()
#     str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
#     hash = hashlib.sha1(str.encode('utf-8')).hexdigest()  # utf-8でエンコードしないとエラーになる
#
#     # トークンをデータベースに追加
#     token = AccessToken.objects.create(
#       user=user,
#       token=hash,
#       access_datetime=dt)
#
#     return token
#
#
#



