# Generated by Django 3.1 on 2020-08-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200826_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
