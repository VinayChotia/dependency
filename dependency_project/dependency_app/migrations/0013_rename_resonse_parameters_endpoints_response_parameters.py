# Generated by Django 5.0.7 on 2024-07-16 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0012_rename_referrer_endpoints_request_parameters_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoints',
            old_name='resonse_parameters',
            new_name='response_parameters',
        ),
    ]