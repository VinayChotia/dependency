# Generated by Django 5.0.7 on 2024-07-15 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0003_remove_endpoints_authentication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoints',
            old_name='path_variables',
            new_name='query_params',
        ),
    ]
