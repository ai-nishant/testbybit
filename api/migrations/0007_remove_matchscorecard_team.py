# Generated by Django 3.1 on 2020-09-01 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_matchscorecard_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchscorecard',
            name='team',
        ),
    ]
