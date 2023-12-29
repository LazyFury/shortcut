# Generated by Django 4.2.7 on 2023-11-29 01:04

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 11, 29, 1, 4, 37, 858987)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qrcode',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='wxqrcode',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wxqrcode',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wxqrcode',
            name='timeout',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 6, 9, 4, 37, 858987), help_text='默认 7 天过期', null=True),
        ),
    ]
