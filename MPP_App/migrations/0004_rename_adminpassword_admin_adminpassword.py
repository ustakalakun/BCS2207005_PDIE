# Generated by Django 4.2.4 on 2024-05-31 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MPP_App', '0003_remove_admin_admin_remove_mpp_mppemail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='adminpassword',
            new_name='adminPassword',
        ),
    ]
