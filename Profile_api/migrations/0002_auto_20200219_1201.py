# Generated by Django 3.0.3 on 2020-02-19 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
