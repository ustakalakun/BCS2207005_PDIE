# Generated by Django 4.2.4 on 2024-05-31 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MPP_App', '0002_rename_student_mpp_rename_studemail_mpp_mppemail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='mpp',
            name='mppEmail',
        ),
        migrations.RemoveField(
            model_name='mpp',
            name='mppName',
        ),
        migrations.RemoveField(
            model_name='mpp',
            name='mppPhone',
        ),
    ]
