# Generated by Django 3.1.5 on 2022-06-12 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20220612_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 16, 19, 43, 305354)),
        ),
    ]
