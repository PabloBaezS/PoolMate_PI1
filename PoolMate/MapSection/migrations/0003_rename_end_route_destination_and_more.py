# Generated by Django 4.1.2 on 2023-05-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MapSection', '0002_alter_route_routeid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='end',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='start',
            new_name='origin',
        ),
        migrations.AddField(
            model_name='route',
            name='routePoints',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
