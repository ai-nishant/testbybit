# Generated by Django 3.1 on 2020-08-26 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200826_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playerscore',
            options={'ordering': ['match']},
        ),
    ]