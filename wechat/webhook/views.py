import hashlib
import hmac
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.conf import settings
from .models import Notification
from .serializers import NotificationSerializer
from .filters import NotificationFilter


def _generate_signature(key, data, signature=''):
    mac = hmac.new(key.encode("utf-8"), msg=data, digestmod=hashlib.sha1)
    return mac.hexdigest() == signature


class WebHookView(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_class = NotificationFilter

    def create(self, request, *args, **kwargs):
        """创建通知"""
        signature = _generate_signature(settings.TAIGA_KEY, json.dumps(request.data).encode('utf8'),
                                        request.META.get('HTTP_X_TAIGA_WEBHOOK_SIGNATURE'))
        if signature:
            return Response('请求非法, 校验失败')
        return super(WebHookView, self).create(request, *args, **kwargs)
