# Generated by Django 5.0.7 on 2024-07-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0014_remove_endpoints_request_parameters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoints',
            name='request_parameters',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='endpoints',
            name='response_parameters',
            field=models.TextField(blank=True),
        ),
    ]