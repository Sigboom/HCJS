from django.db import models
from django.db.models import BooleanField as _BooleanField


class BooleanField(_BooleanField):
    def get_prep_value(self, value):
        if value in ("0", "false", "False"):
            return False
        elif value in ("1", "true", "True"):
            return True
        else:
            return super(BooleanField, self).get_prep_value(value)

class Message(models.Model):
    userFrom = models.ForeignKey('sign_io.User', related_name='userFrom', on_delete=models.CASCADE)
    userTo = models.ForeignKey('sign_io.User', related_name='userTo', on_delete=models.CASCADE)
    message = models.CharField('message', max_length=300)
    msgTime = models.DateTimeField('msgTime')
    msgType = models.IntegerField('msgType', default=0)
    # 0 个人信息无需回复 1 个人需回复
    # 10 团队信息无需回复 11 团队信息需回复
    # 20 系统消息无需回复 21 系统消息需回复
    msgBits = models.IntegerField('msgBits', default=0)
    class Meta:
        db_table = 'message'

class Follower(models.Model):
    follower = models.ForeignKey('sign_io.User', related_name='follower', on_delete=models.CASCADE)
    user = models.ForeignKey('sign_io.User', related_name='user', on_delete=models.CASCADE)
    class Meta:
        db_table = 'follower'
        unique_together=("user", "follower",)
