# Generated by Django 5.0.6 on 2024-06-14 00:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0002_alter_item_unique_together_item_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="image_tags",
        ),
    ]