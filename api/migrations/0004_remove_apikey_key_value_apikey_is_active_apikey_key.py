# Generated by Django 4.2.1 on 2023-05-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_apikey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='key_value',
        ),
        migrations.AddField(
            model_name='apikey',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=2498, max_length=100),
            preserve_default=False,
        ),
    ]