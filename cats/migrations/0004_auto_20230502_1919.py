# Generated by Django 3.2 on 2023-05-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20230502_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievementcat',
            old_name='achievement',
            new_name='achievements',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='achievement',
            new_name='achievements',
        ),
    ]