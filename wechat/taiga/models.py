from django.db import models
from django.contrib.auth import get_user_model
import jsonfield

# Create your models here.
User = get_user_model()


class UserInfo(models.Model):
    nickname = models.CharField('微信昵称', max_length=64, default='', null=True, blank=True)
    avatar_url = models.URLField('微信头像链接', max_length=128, default='', null=True, blank=True)
    country = models.CharField('国家', max_length=32, default='', null=True, blank=True)
    province = models.CharField('省份', max_length=32, default='', null=True, blank=True)
    city = models.CharField('城市', max_length=32, default='', null=True, blank=True)
    gender = models.CharField('性别', max_length=8, default='', null=True, blank=True)
    language = models.CharField('语言', max_length=32, default='', null=True, blank=True)

    class Meta:
        verbose_name = '微信的userInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.id, self.nickname)


class TaigaUser(models.Model):
    user = models.ForeignKey(User, on_delete=False, null=True, blank=True)
    user_info = models.ForeignKey(UserInfo, on_delete=False, null=True, blank=True)

    openid = models.CharField('微信开放id', max_length=64)
    session_key = models.CharField('微信session key', max_length=64)

    bearer = models.CharField('taiga token', max_length=64, null=True, blank=True)
    related_id = models.CharField('关联id', max_length=256, null=True, blank=True)  # (备用)
    extra = jsonfield.JSONField('扩展数据')

    # extrat = models

    class Meta:
        verbose_name = '微信用户Taiga关联'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.openid, self.session_key)
