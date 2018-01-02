# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='assetType',
            new_name='asset_type',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='businessUnit',
            new_name='business_unit',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='domainRole',
            new_name='domain_role',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='dynamicIp',
            new_name='dynamic_ip',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='hardwareAgent',
            new_name='hardware_agent',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='hostName',
            new_name='host_name',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='ipAddress',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='lastBoot',
            new_name='last_boot',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='operatingSystem',
            new_name='operating_system',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='osVersion',
            new_name='os_version',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='serialNumber',
            new_name='serial_number',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='systemName',
            new_name='system_name',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='warrantyStatus',
            new_name='warranty_status',
        ),
    ]