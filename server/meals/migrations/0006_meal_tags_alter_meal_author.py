# Generated by Django 5.1.3 on 2024-12-14 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0005_remove_meal_tags"),
        ("tags", "0002_tag_inheritance_and_logic"),
        ("users", "0002_user_is_active_user_is_staff_user_is_superuser_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="tags",
            field=models.ManyToManyField(blank=True, to="tags.tag"),
        ),
        migrations.AlterField(
            model_name="meal",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.user",
            ),
        ),
    ]
