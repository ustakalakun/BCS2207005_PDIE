# Generated by Django 4.2.4 on 2024-06-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MPP_App', '0005_delete_mpp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPP',
            fields=[
                ('mppId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mpppassword', models.CharField(max_length=15)),
                ('mppname', models.CharField(max_length=20)),
            ],
        ),
    ]
