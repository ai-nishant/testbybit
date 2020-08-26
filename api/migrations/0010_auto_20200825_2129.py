# Generated by Django 3.1 on 2020-08-25 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200825_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team',
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1', to='api.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2', to='api.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='looser',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='looser', to='api.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to='api.team'),
        ),
    ]
