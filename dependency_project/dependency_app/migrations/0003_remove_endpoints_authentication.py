# Generated by Django 5.0.7 on 2024-07-15 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0002_remove_endpoints_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoints',
            name='authentication',
        ),
    ]
