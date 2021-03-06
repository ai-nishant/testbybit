# Generated by Django 3.1 on 2020-08-26 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200826_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchscorecard',
            name='bounce',
        ),
        migrations.RemoveField(
            model_name='matchscorecard',
            name='four',
        ),
        migrations.RemoveField(
            model_name='matchscorecard',
            name='six',
        ),
        migrations.RemoveField(
            model_name='matchscorecard',
            name='wide',
        ),
        migrations.RemoveField(
            model_name='player',
            name='playerscore',
        ),
        migrations.AddField(
            model_name='matchscorecard',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='matchscorecard',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Playerscore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('wide', models.IntegerField(blank=True, null=True)),
                ('bounce', models.IntegerField(blank=True, null=True)),
                ('four', models.IntegerField(blank=True, null=True)),
                ('six', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.match')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.player')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.team')),
            ],
        ),
    ]
