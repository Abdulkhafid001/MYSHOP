# Generated by Django 4.2.2 on 2023-11-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptechteam', '0005_alter_members_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='image_name',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]
