from django.db import models

class Teams(models.Model):
    teamId = models.IntegerField(primary_key=True)
    teamName = models.CharField('teamName', unique=True, max_length=20)    
    owner = models.ForeignKey('sign_io.User', on_delete=models.CASCADE)
    buildTime = models.DateTimeField('buildTime')
    memberMax = models.IntegerField('memberMax', default=10)
    headPic = models.CharField('headPic', default="../../../assets/default-head.jpg", max_length=255)
    notice = models.CharField('notice', max_length=255, blank=True)
    teamType = models.IntegerField('teamType', default=0)
    class Meta:
        db_table = 'teams'

class UserTeam(models.Model):
    teammap = models.ForeignKey('Teams', on_delete=models.CASCADE)
    member = models.ForeignKey('sign_io.User', on_delete=models.CASCADE)
    class Meta:
        db_table = 'userTeam'
        unique_together=["teammap", "member"]

class TeamFile(models.Model):
    teammap = models.ForeignKey('Teams', on_delete=models.CASCADE)
    filemap = models.ForeignKey('fileManager.FileMap', on_delete=models.CASCADE)
    teamDirId = models.IntegerField('teamDirId', default=0)
    class Meta:
        db_table = 'teamFiles'
