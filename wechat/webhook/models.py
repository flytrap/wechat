from django.db import models
import jsonfield


class Notification(models.Model):
    ACTION_CHOICES = (
        ('create', '新建'),
        ('change', '修改'),
        ('delete', '删除'),
        ('test', '测试')
    )
    TYPE_CHOICES = (
        ('milestone', '里程碑'),
        ('userstory', '用户故事'),
        ('task', '任务'),
        ('issue', '问题'),
        ('wikipage', 'wikipage'),
        ('test', '测试')
    )
    project_id = models.IntegerField('项目id', null=True, blank=True)
    type = models.CharField('类型', choices=TYPE_CHOICES, max_length=32)
    action = models.CharField('操作类型', choices=ACTION_CHOICES, max_length=32)
    by = jsonfield.JSONField('操作人', null=True, blank=True)
    date = models.DateTimeField('操作时间', null=True, blank=True)
    data = jsonfield.JSONField('负载数据', null=True, blank=True)
    change = jsonfield.JSONField('变化对比', null=True, blank=True)

    is_read = models.BooleanField('已读', default=False)

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return '{} {} {}'.format(self.id, self.action, self.type)
