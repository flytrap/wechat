#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name='_get_title')
    content = serializers.SerializerMethodField(method_name='_get_content')
    desc = serializers.SerializerMethodField(method_name='_get_desc')
    by = serializers.JSONField(required=False)
    data = serializers.JSONField(required=False, write_only=True)
    change = serializers.JSONField(required=False, write_only=True)
    created = serializers.SerializerMethodField(method_name='_get_date')

    class Meta:
        model = Notification
        fields = '__all__'

    @staticmethod
    def _get_title(obj):
        return '{} {} {}'.format(obj.by.get('full_name'), obj.action, obj.type)

    @staticmethod
    def _get_content(obj):
        project_name = obj.data.get('project', {}).get('name', '') if obj.data.get('project') else ''
        subject = obj.data.get('subject', obj.data.get('name', ''))
        return '{}: {}-{}'.format(obj.type, project_name, subject)

    @staticmethod
    def _get_desc(obj):
        results = ''
        if obj.change:
            for k, v in obj.change.get('diff', {}).items():
                if isinstance(v, str):
                    results += '{}: {}'.format(k, v)
                    continue
                results += '{}: {}->{};'.format(k, v.get('from'), v.get('to'))
        return results

    @staticmethod
    def _get_date(obj):
        return obj.date.strftime('%y-%m-%d-%R:%S')

    def create(self, validated_data):
        validated_data['project_id'] = validated_data.get('data', {}).get('project', {}).get('id')
        return super(NotificationSerializer, self).create(validated_data)
