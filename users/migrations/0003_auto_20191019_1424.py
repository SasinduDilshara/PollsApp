# Generated by Django 2.2.5 on 2019-10-19 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191019_1424'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appuser',
            unique_together={('number', 'snippet')},
        ),
    ]
