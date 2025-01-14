# Generated by Django 5.1.4 on 2024-12-17 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_plan', '0007_alter_dietplan_author'),
        ('users', '0004_alter_user_diet_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='diet_plan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_plan.dietplan'),
        ),
    ]
