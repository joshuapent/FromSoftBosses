# Generated by Django 4.1.7 on 2023-04-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='image',
        ),
        migrations.RemoveField(
            model_name='boss',
            name='ishard',
        ),
        migrations.RemoveField(
            model_name='boss',
            name='resistances',
        ),
        migrations.RemoveField(
            model_name='boss',
            name='weaknesses',
        ),
        migrations.AddField(
            model_name='game',
            name='weaknesses',
            field=models.ManyToManyField(to='main_app.weakness'),
        ),
    ]