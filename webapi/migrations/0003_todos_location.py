# Generated by Django 4.2 on 2023-04-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0002_todos'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
