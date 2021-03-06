# Generated by Django 2.0.4 on 2020-05-20 13:02

from django.db import migrations, models
import django.db.models.deletion
import fileManager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sign_io', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileMap',
            fields=[
                ('fileId', models.IntegerField(primary_key=True, serialize=False)),
                ('filePath', models.CharField(max_length=255, unique=True, verbose_name='filePath')),
                ('fileType', models.IntegerField(default=0, verbose_name='fileType')),
                ('fileField', models.FileField(blank=True, null=True, upload_to=fileManager.models.get_media_upload_to, verbose_name='file')),
                ('fileMd5', models.CharField(max_length=255, unique=True, verbose_name='fileMd5')),
                ('buildTime', models.DateTimeField(verbose_name='buildTime')),
                ('modTime', models.DateTimeField(verbose_name='modTime')),
                ('readTime', models.DateTimeField(verbose_name='readTime')),
                ('ownermap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign_io.User')),
            ],
            options={
                'db_table': 'fileMap',
            },
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commitMsg', models.CharField(max_length=300, verbose_name='commitMsg')),
                ('star', fileManager.models.BooleanField(default=False, verbose_name='star')),
                ('fileName', models.CharField(max_length=200, verbose_name='fileName')),
                ('dirId', models.IntegerField(default=0, verbose_name='dirId')),
                ('filemap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileManager.FileMap')),
                ('usermap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign_io.User')),
            ],
            options={
                'db_table': 'userFiles',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userfile',
            unique_together={('dirId', 'fileName')},
        ),
    ]
