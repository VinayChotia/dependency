# Generated by Django 5.0.7 on 2024-07-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0007_rename_parameters_endpoints_headers'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoints',
            name='authentication',
            field=models.TextField(blank=True, null=True),
        ),
    ]
