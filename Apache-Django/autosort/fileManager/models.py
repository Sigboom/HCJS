from django.db import models
from django.conf import settings
import os

from django.db.models import BooleanField as _BooleanField

class BooleanField(_BooleanField):
    def get_prep_value(self, value):
        if value in ("0", "false", "False"):
            return False
        elif value in ("1", "true", "True"):
            return True
        else:
            return super(BooleanField, self).get_prep_value(value)


class UserFile(models.Model):
    filemap = models.ForeignKey('FileMap', on_delete=models.CASCADE)
    usermap = models.ForeignKey('sign_io.User', on_delete=models.CASCADE)
    commitMsg = models.CharField('commitMsg', max_length=300, blank=True)
    star = BooleanField('star', default=False)
    fileName = models.CharField('fileName', max_length=255)
    dirId = models.IntegerField('dirId', default=0)
    fileClass = models.IntegerField('fileClass', default=-1)
    class Meta:
        db_table = 'userFiles'
        unique_together=("usermap", "filemap",)
        unique_together=("dirId", "fileName",)

def get_media_upload_to(instance, fileName):
    return os.path.join(settings.MEDIA_ROOT, str(instance.ownermap.userId), fileName)

class FileMap(models.Model):
    fileId = models.IntegerField(primary_key=True)
    ownermap = models.ForeignKey('sign_io.User', on_delete=models.CASCADE)
    filePath = models.CharField('filePath', max_length=255, unique=True)
    fileType = models.IntegerField('fileType', default=0)
    fileField = models.FileField('file', upload_to=get_media_upload_to, blank=True, null=True)
    fileMd5 = models.CharField('fileMd5', max_length=255)
    buildTime = models.DateTimeField('buildTime')
    modTime = models.DateTimeField('modTime')
    readTime = models.DateTimeField('readTime')
    class Meta:
        db_table = 'fileMap'
