#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
import hashlib

from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse
from django.conf import settings


class CheckWeChat(GenericViewSet):
    def get(self, request, *args, **kwargs):
        """
        验证来自微信服务器的请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        token = getattr(settings, 'WECHAT', {}).get('token', '')

        # 计算排序后的哈希值并比较
        sig = hashlib.sha1(''.join(sorted([token, timestamp, nonce])).encode()).hexdigest()
        if sig == signature:
            return HttpResponse(request.GET.get('echostr', ''), content_type='text/plain')
        return HttpResponse('error')
