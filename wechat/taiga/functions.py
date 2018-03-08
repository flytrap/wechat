#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
import json
import requests
from django.conf import settings

# 使用远程调用方式登录
CHAT_SETTING = getattr(settings, 'CHAT_SETTING', {})
REMOTE = CHAT_SETTING.get('REMOTE', True)
REMOTE_INDEX = CHAT_SETTING.get('REMOTE_INDEX', True)


def login(request, username, password, **kwargs):
    data = {
        "username": username,
        "password": password,
        "type": "normal"
    }
    if REMOTE and REMOTE_INDEX:
        response = requests.post('{}/{}'.format(REMOTE_INDEX, 'api/v1/auth'), data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})
        results = response.json()
    else:
        try:
            from taiga.auth.services import normal_login_func
            results = normal_login_func(request)
        except ImportError as e:
            print(e)
            results = {}
    return results


def check_token(token):
    if not token:
        return False
    if REMOTE and REMOTE_INDEX:
        response = requests.get('{}/{}'.format(REMOTE_INDEX, 'api/v1/projects'),
                                headers={
                                    'Authorization': 'Bearer {}'.format(token)
                                })
        data = response.json()
        if '_error_message' in data:
            return False
    else:
        max_age_auth_token = getattr(settings, "MAX_AGE_AUTH_TOKEN", None)
        try:
            from taiga.auth.tokens import get_user_for_token
            user = get_user_for_token(token, "authentication",
                                      max_age=max_age_auth_token)
        except ImportError:
            return False
        except Exception as e:
            # if 'Invalid token' in e.args[0]:
            return False
    return True
