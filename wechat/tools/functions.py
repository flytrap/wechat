#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
import requests


class XCX(object):
    code_to_session = 'https://api.weixin.qq.com/sns/jscode2session'

    def __init__(self, appid, secret, *args, **kwargs):
        self.appid = appid,
        self.secret = secret

    def get_session(self, code):
        params = {
            'appid': self.appid,
            'secret': self.secret,
            'js_code': code,
        }
        response = requests.get(self.code_to_session, params)
        data = response.json()
        print(data)
        return data
