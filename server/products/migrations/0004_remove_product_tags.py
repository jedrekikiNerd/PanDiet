# Generated by Django 5.1.3 on 2024-12-13 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="tags",
        ),
    ]
