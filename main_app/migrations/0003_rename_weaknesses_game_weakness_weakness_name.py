# Generated by Django 4.1.7 on 2023-04-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_boss_image_remove_boss_ishard_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='weaknesses',
            new_name='weakness',
        ),
        migrations.AddField(
            model_name='weakness',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]