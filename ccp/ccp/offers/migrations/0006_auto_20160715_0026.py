# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 00:26
from __future__ import unicode_literals

from django.db import migrations
import sizefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_auto_20160714_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='disk_size',
            field=sizefield.models.FileSizeField(help_text='Put values in MB, GB or TB. Eg.: 20GB, 40GB, 1TB.', verbose_name='Disk size'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='memory_size',
            field=sizefield.models.FileSizeField(help_text='Put values in MB, GB or TB. Eg.: 512MB, 1024MB, 2GB.', verbose_name='Memory size'),
        ),
    ]