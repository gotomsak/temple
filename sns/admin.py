from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


class SpeakerInline(admin.StackedInline):
  model = Speaker
  can_delete = False
  varbose_name_plural = 'speaker'


class UserAdmin(BaseUserAdmin):
  inlines = (SpeakerInline,)


class AccessTokenAdmin(admin.ModelAdmin):
  fields = ['user', 'token', 'access_datetime']


admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Position)
admin.site.register(Belong)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

