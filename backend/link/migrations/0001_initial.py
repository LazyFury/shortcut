# Generated by Django 4.2.7 on 2023-11-26 12:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('url', models.URLField(max_length=2000, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sortUrl', models.CharField(blank=True, max_length=10, unique=True)),
                ('clickCount', models.IntegerField(default=0, editable=False)),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '短链',
                'verbose_name_plural': '短链',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='WXQRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('qrcode', models.ImageField(upload_to='uploads//qrcode/wx/')),
                ('type', models.IntegerField(choices=[(1, '微信好友'), (2, '微信群')], default=1)),
                ('timeout', models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 3, 20, 17, 48, 205480), help_text='默认 7 天过期', null=True)),
                ('remind', models.IntegerField(choices=[(1, '微信提醒'), (2, '邮件提醒')], default=1)),
                ('desc', models.CharField(blank=True, max_length=400)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '微信二维码',
                'verbose_name_plural': '微信二维码',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='VisitorIP',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='link.link')),
            ],
            options={
                'verbose_name': '短链访客IP记录',
                'verbose_name_plural': '短链访客IP记录',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originUrl', models.URLField(blank=True, max_length=2000, null=True)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, editable=False, upload_to='')),
                ('type', models.CharField(choices=[('URL', '超链接'), ('TEXT', '文本'), ('WX', '微信二维码')], default='URL', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('short', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='short_qrcode_set', to='link.link')),
                ('wx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wx_qrcode_set', to='link.wxqrcode')),
            ],
            options={
                'verbose_name': '二维码',
                'verbose_name_plural': '二维码',
                'ordering': ['-id'],
            },
        ),
    ]