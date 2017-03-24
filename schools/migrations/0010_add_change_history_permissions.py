# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20150605_0745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='addresslocation',
            options={'managed': True, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'address location', 'verbose_name_plural': 'address locations'},
        ),
        migrations.AlterModelOptions(
            name='archivedata',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'archive data', 'verbose_name_plural': 'archive datas'},
        ),
        migrations.AlterModelOptions(
            name='archivedatalink',
            options={'managed': True, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'archive data link', 'verbose_name_plural': 'archive data link'},
        ),
        migrations.AlterModelOptions(
            name='building',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'building', 'verbose_name_plural': 'buildings'},
        ),
        migrations.AlterModelOptions(
            name='buildingaddress',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'building address', 'verbose_name_plural': 'building addresses'},
        ),
        migrations.AlterModelOptions(
            name='buildingname',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='buildingownership',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='employership',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'employership', 'verbose_name_plural': 'employerships'},
        ),
        migrations.AlterModelOptions(
            name='lifecycleevent',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'lifecycle event', 'verbose_name_plural': 'lifecycle events'},
        ),
        migrations.AlterModelOptions(
            name='nametype',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'name type', 'verbose_name_plural': 'name types'},
        ),
        migrations.AlterModelOptions(
            name='neighborhood',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='numberofgrades',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='ownerfounder',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='principal',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'principal', 'verbose_name_plural': 'principals'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'school', 'verbose_name_plural': 'schools'},
        ),
        migrations.AlterModelOptions(
            name='schoolbuilding',
            options={'managed': False, 'ordering': ['school'], 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'school building', 'verbose_name_plural': 'school buildings'},
        ),
        migrations.AlterModelOptions(
            name='schoolbuildingphoto',
            options={'managed': True, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'school building photo', 'verbose_name_plural': 'school building photos'},
        ),
        migrations.AlterModelOptions(
            name='schoolcontinuum',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'continuum event', 'verbose_name_plural': 'continuum events'},
        ),
        migrations.AlterModelOptions(
            name='schoolfield',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='schoolfounder',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='schoolgender',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='schoollanguage',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='schoolname',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'school name', 'verbose_name_plural': 'school names'},
        ),
        migrations.AlterModelOptions(
            name='schoolownership',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),)},
        ),
        migrations.AlterModelOptions(
            name='schooltype',
            options={'managed': False, 'permissions': (('change_history', 'Can change historical records'),), 'verbose_name': 'school type', 'verbose_name_plural': 'school types'},
        ),
        migrations.AlterField(
            model_name='addresslocation',
            name='handmade',
            field=models.BooleanField(default=False, help_text='Select this if you want to update the location manually. Otherwise, the location will update automatically when you change the address.', verbose_name='Update location by hand'),
        ),
        migrations.AlterField(
            model_name='schoolbuildingphoto',
            name='is_front',
            field=models.BooleanField(default=True, help_text='Is this a picture of the building front?', verbose_name='is_front'),
        ),
    ]
