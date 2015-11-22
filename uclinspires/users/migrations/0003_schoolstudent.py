# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151122_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_profile', models.OneToOneField(to='users.UserProfile')),
            ],
        ),
    ]
