# Generated by Django 5.0.7 on 2024-07-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0015_endpoints_request_parameters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoints',
            name='referrer',
            field=models.TextField(blank=True),
        ),
    ]