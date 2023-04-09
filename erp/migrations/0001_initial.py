# Generated by Django 4.2 on 2023-04-09 05:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        choices=[
                            ("hood-001", "hood-001"),
                            ("hood-002", "hood-002"),
                            ("hood-003", "hood-003"),
                            ("jean-001", "jean-001"),
                        ],
                        max_length=8,
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("description", models.CharField(default="상품설명 입력", max_length=256)),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                            ("X", "XLarge"),
                            ("F", "Free"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "db_table": "product",
            },
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="erp.productmodel",
                    ),
                ),
                (
                    "stock_count",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "inventory",
            },
        ),
        migrations.CreateModel(
            name="OutBound",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("outbound_date", models.DateField(auto_now_add=True)),
                (
                    "cost",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "code_name_size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="erp.inventory"
                    ),
                ),
            ],
            options={
                "db_table": "outbound",
            },
        ),
        migrations.CreateModel(
            name="InBound",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inbound_date", models.DateField(auto_now_add=True)),
                (
                    "cost",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "code_name_size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="erp.inventory"
                    ),
                ),
            ],
            options={
                "db_table": "inbound",
            },
        ),
    ]