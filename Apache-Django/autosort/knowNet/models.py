from django.db import models

class FileNode(models.Model):
    filemap = models.ForeignKey('fileManager.FileMap', on_delete=models.CASCADE)
    classVector = models.CharField('classVector', max_length=255)
    class Meta:
        db_table = 'fileNodes'
        

class UserNode(models.Model):
    usermap = models.ForeignKey('sign_io.User', on_delete=models.CASCADE)
    classVector = models.CharField('classVector', max_length=255)
    class Meta:
        db_table = 'userNodes'


class NodeMap(models.Model):
    fnodemap = models.ForeignKey('FileNode', on_delete=models.CASCADE)
    unodemap = models.ForeignKey('UserNode', on_delete=models.CASCADE) 
    nodeName = models.CharField('nodeName', max_length=255)
    nodeValue = models.IntegerField('nodeValue')
    class Meta:
        db_table = 'nodeMap'
