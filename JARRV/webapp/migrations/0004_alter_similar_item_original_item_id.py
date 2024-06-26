# Generated by Django 5.0.6 on 2024-06-17 04:26

import django.db.models.deletion
import webapp.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0003_alter_similar_item_original_item_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="similar_item",
            name="original_item_id",
            field=models.ForeignKey(
                default=webapp.models.get_default_item,
                on_delete=django.db.models.deletion.CASCADE,
                to="webapp.item",
            ),
        ),
    ]
