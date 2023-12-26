# Generated by Django 4.2.5 on 2023-10-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stockMgmt", "0003_companyname"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockMgmt",
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
                ("protype_id", models.IntegerField()),
                ("proname_id", models.IntegerField()),
                ("comname_id", models.IntegerField()),
                ("stock_type", models.CharField(max_length=50)),
                ("dealer_name", models.CharField(max_length=100)),
                (
                    "dealer_mobile",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("dealer_address", models.TextField()),
                ("date_field", models.DateField()),
                (
                    "product_weight",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("product_quantity", models.IntegerField()),
                (
                    "purchase_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
