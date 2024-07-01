# Generated by Django 5.0.6 on 2024-07-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0015_remove_user_first_name_remove_user_is_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
    ]
