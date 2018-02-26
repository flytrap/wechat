#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
import json
import time
import requests
import weixin

TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token'
USER_INFO = 'https://api.weixin.qq.com/cgi-bin/user/info'
USER_LIST = 'https://api.weixin.qq.com/cgi-bin/user/get'


class WeChat(object):
    def __init__(self, appid, secret):
        self.appid = appid
        self.secret = secret

        self.access_token = None
        self.token_time = time.time()

        self.response = None
        self.data = None
        self.error = None

    def get_token(self):
        params = {
            'grant_type': 'client_credential',
            'appid': self.appid,
            'secret': self.secret
        }
        self.response = requests.get(TOKEN_URL, params)
        if self.get_data():
            self.access_token = self.data.get('access_token')
            self.token_time = time.time()
            return self.access_token

    def get_user_info(self, openid, lang='zh_CN'):
        """获取用户信息"""
        self.checkout_token()
        params = {
            'access_token': self.access_token,
            'openid': openid,
            'lang': lang
        }
        self.response = requests.get(USER_INFO, params=params)
        if self.get_data():
            return self.data

    def get_user_list(self, next_openid=None):
        """获取用户列表"""
        self.checkout_token()
        params = {
            'access_token': self.access_token
        }
        if next_openid:
            params['next_openid'] = next_openid
        self.response = requests.get(USER_LIST, params=params)
        if self.get_data():
            return self.data

    def checkout_token(self):
        """检查token有效性， 无效则获取"""
        if not self.access_token or time.time() - self.token_time >= 7000:
            self.get_token()

    def get_data(self):
        assert hasattr(self.response, 'content'), 'error response'
        self.data = json.loads(self.response.content)
        if 'errmsg' not in self.data:
            return True
        self.error = self.data.get('errmsg')
        return False


if __name__ == '__main__':
    we_chat = WeChat('', '')
    token = we_chat.get_token()
    data = we_chat.get_user_list()
    print(data)
