# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='u_name',
            field=models.CharField(help_text=b'\xe6\x88\xb7\xe4\xb8\xbb\xe5\xa7\x93\xe5\x90\x8d', max_length=20, verbose_name=b'\xe6\x88\xb7\xe4\xb8\xbb\xe5\xa7\x93\xe5\x90\x8d'),
        ),
    ]
