# Generated by Django 5.0.1 on 2024-01-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_telegramuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Телефонный номер'),
            preserve_default=False,
        ),
    ]
