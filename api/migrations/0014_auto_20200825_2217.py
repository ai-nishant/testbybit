# Generated by Django 3.1 on 2020-08-25 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200825_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchscorecard',
            name='match',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.match'),
        ),
        migrations.AddField(
            model_name='matchscorecard',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_type',
            field=models.CharField(blank=True, choices=[('test match', 'TEST MATCH'), ('one day international', 'ONE DAY INTERNATIONAL'), ('twenty 20 world cup', 'TWENTY 20 WORLD CUP')], max_length=40, null=True),
        ),
    ]
