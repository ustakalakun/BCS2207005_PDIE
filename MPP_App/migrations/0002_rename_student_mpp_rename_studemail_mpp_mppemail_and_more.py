# Generated by Django 4.2.4 on 2024-05-31 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MPP_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='STUDENT',
            new_name='MPP',
        ),
        migrations.RenameField(
            model_name='mpp',
            old_name='studEmail',
            new_name='mppEmail',
        ),
        migrations.RenameField(
            model_name='mpp',
            old_name='studId',
            new_name='mppId',
        ),
        migrations.RenameField(
            model_name='mpp',
            old_name='studName',
            new_name='mppName',
        ),
        migrations.RenameField(
            model_name='mpp',
            old_name='studPhone',
            new_name='mppPhone',
        ),
        migrations.RenameField(
            model_name='mpp',
            old_name='studpassword',
            new_name='mpppassword',
        ),
    ]
