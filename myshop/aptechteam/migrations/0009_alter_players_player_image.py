# Generated by Django 4.2.2 on 2023-11-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptechteam', '0008_alter_players_player_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='player_image',
            field=models.ImageField(blank=True, height_field=40, null=True, upload_to='media/', width_field=40),
        ),
    ]
