# Generated by Django 3.1.5 on 2022-06-12 16:13

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_json', jsonfield.fields.JSONField()),
            ],
        ),
    ]
