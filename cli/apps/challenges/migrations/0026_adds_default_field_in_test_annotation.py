# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-10 19:23
from __future__ import unicode_literals

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0025_added_is_submission_pubblic_field")]

    operations = [
        migrations.AlterField(
            model_name="challengephase",
            name="test_annotation",
            field=models.FileField(
                default=False,
                upload_to=base.utils.RandomFileName("test_annotations"),
            ),
        )
    ]