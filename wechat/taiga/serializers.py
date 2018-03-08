#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django.conf import settings
from rest_framework import serializers
from .models import UserInfo, TaigaUser
from .functions import check_token, login


class UserInfoSerializer(serializers.ModelSerializer):
    nickName = serializers.CharField(source='nickname', help_text='昵称')
    avatarUrl = serializers.CharField(source='avatar_url', help_text='头像链接')

    class Meta:
        model = UserInfo
        fields = ('nickName', 'avatarUrl', 'country', 'province', 'city', 'gender', 'language')


class TaigaUserSerializer(serializers.Serializer):
    related_id = serializers.IntegerField(required=False, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    userInfo = UserInfoSerializer(many=False, label='用户信息', write_only=True)
    code = serializers.CharField(write_only=True)
    bearer = serializers.CharField(read_only=True)

    def create(self, validated_data):
        from tools.functions import XCX
        chat_data = getattr(settings, 'WECHAT', {})
        xcy = XCX(**chat_data)
        data = xcy.get_session(code=validated_data.get('code'))
        taiga_user = TaigaUser.objects.filter(openid=data.get('openid')).first()
        # 测试token是否有效
        results = None
        bearer = taiga_user.bearer if taiga_user else None
        if not check_token(bearer):
            # 尝试登录, 登录过一般就不需要了
            results = login(self._context.get('request'), username=validated_data.get('username', ''),
                            password=validated_data.get('password', ''))
        if not taiga_user:
            user_info, _ = UserInfo.objects.get_or_create(**validated_data.get('userInfo', {}))
            taiga_user = TaigaUser.objects.create(user_info=user_info, **data)
        if results and 'auth_token' in results:
            # 更新token
            taiga_user.bearer = results.get('auth_token', '')
            taiga_user.related_id = results.get('id')
            taiga_user.extra = results
            taiga_user.save()

        taiga_user.username = taiga_user.extra.get('full_name', '')
        self.instance = taiga_user
        return taiga_user

    def update(self, instance, validated_data):
        from tools.functions import XCX
        chat_data = getattr(settings, 'WECHAT', {})
        xcy = XCX(**chat_data)
        data = xcy.get_session(code=validated_data.get('code'))
        taiga_user = TaigaUser.objects.filter(openid=data.get('openid')).first()
        if taiga_user:
            taiga_user.bearer = None
            taiga_user.save()
