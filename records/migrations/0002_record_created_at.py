# Generated by Django 5.1.1 on 2024-09-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]