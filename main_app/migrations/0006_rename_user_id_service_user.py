# Generated by Django 4.2.2 on 2023-08-10 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_user_service_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='user_id',
            new_name='user',
        ),
    ]