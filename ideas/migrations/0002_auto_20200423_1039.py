# Generated by Django 2.2.5 on 2020-04-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
