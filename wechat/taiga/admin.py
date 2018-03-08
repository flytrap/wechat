from django.contrib import admin
from .models import TaigaUser, UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'country', 'province', 'city')


@admin.register(TaigaUser)
class TaigaUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'openid', 'session_key', 'bearer', 'related_id')
