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

