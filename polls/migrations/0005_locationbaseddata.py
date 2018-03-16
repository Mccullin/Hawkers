# Generated by Django 2.0.2 on 2018-03-14 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationBasedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('hotspotRadius', models.IntegerField()),
                ('visitorCount', models.IntegerField()),
                ('trailInfo', models.TextField()),
            ],
        ),
    ]