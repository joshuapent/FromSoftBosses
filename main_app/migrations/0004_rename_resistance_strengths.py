# Generated by Django 4.1.7 on 2023-04-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_weaknesses_game_weakness_weakness_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resistance',
            new_name='Strengths',
        ),
    ]
