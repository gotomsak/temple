from django.db import models
from django.utils import timezone
import hashlib
from datetime import timedelta

from django.contrib.auth.models import User

# Create your models here.


# 支部名を入れるテーブル
class Belong(models.Model):

  belong_text = models.CharField(max_length=30)


# 部を入れるテーブル
class Position(models.Model):
  position_text = models.CharField(max_length=50)



# 講員をUserに追加
class Speaker(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image_path = models.ImageField(max_length=100)
  notice_auth = models.BooleanField(default=False)
  position = models.ForeignKey(Position, on_delete=models.CASCADE)
  status_message = models.CharField(max_length=100)
  belong = models.ForeignKey(Belong, on_delete=models.CASCADE)


# AccessTokenのテーブル
class AccessToken(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  token = models.CharField(max_length=40)
  access_datetime = models.DateTimeField()

  def __str__(self):
    # メールアドレスとアクセス日時、トークンが見えるようにする
    dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
    return self.user.email + '(' + dt + ') - ' + self.token


  @staticmethod
  def create(user: User):
    # ユーザの既存のトークンを取得
    if AccessToken.objects.filter(user=user).exists():
      # トークンが既に存在している場合は削除する
      AccessToken.objects.get(user=user).delete()

    # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
    dt = timezone.now()
    str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
    hash = hashlib.sha1(str.encode('utf-8')).hexdigest()  # utf-8でエンコードしないとエラーになる

    # トークンをデータベースに追加
    token = AccessToken.objects.create(
      user=user,
      token=hash,
      access_datetime=dt)

    return token

  @staticmethod
  def get(token_str: str):
    # 引数のトークン文字列が存在するかチェック
    if AccessToken.objects.filter(token=token_str).exists():
      # 存在した場合はトークンを返却
      return AccessToken.objects.get(token=token_str)
    else:
      # 存在しない場合はNoneを返却
      return None

  def check_valid_token(self):
    # このトークンが有効かどうかをチェック
    delta = timedelta(minutes=30)  # 有効時間は30分
    if (delta < timezone.now() - self.access_datetime):
      # 最終アクセス時間から30分以上経過している場合はFalseを返却
      return False

    return True

  def update_access_datetime(self):
    # 最終アクセス日時を現在日時で更新
    self.access_datetime = timezone.now()
    self.save()





