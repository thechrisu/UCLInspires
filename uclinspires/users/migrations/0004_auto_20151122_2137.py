# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_schoolstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFollowsUniStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_student', models.ForeignKey(to='users.UserProfile')),
                ('uni_student', models.ForeignKey(related_name='following', to='users.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='schoolstudent',
            name='interests',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
