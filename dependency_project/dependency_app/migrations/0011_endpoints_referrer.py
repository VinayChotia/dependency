# Generated by Django 5.0.7 on 2024-07-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app', '0010_remove_endpoints_dependencies'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoints',
            name='referrer',
            field=models.TextField(blank=True),
        ),
    ]
