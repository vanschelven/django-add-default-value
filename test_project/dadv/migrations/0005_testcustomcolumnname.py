# Generated by Django 3.1.3 on 2020-11-05 16:38

from django.db import migrations, models
from django_add_default_value import AddDefaultValue


class Migration(migrations.Migration):

    dependencies = [
        ("dadv", "0004_time_related_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestCustomColumnName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        db_column="custom_id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "is_functional",
                    models.BooleanField(db_column="custom_field", default=False),
                ),
            ],
        ),
        AddDefaultValue(
            model_name="TestCustomColumnName", name="is_functional", value=False
        ),
    ]
