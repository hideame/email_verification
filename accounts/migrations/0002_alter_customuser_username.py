# Generated by Django 4.2.8 on 2023-12-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=150, verbose_name="username"),
        ),
    ]
