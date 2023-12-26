# Generated by Django 4.2.4 on 2023-08-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyProfileModel",
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
                ("company_name", models.CharField(max_length=255)),
                ("website", models.CharField(max_length=255)),
                ("company_email", models.EmailField(max_length=254)),
                ("account_email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("pincode", models.IntegerField()),
                ("pan_number", models.CharField(max_length=255)),
                ("pan_file", models.CharField(blank=True, max_length=255, null=True)),
                ("gst_number", models.CharField(max_length=255)),
                ("gst_file", models.CharField(blank=True, max_length=255, null=True)),
                ("iec_code", models.CharField(max_length=255)),
                ("logo", models.CharField(blank=True, max_length=255, null=True)),
                ("iso_certificate_number", models.CharField(max_length=255)),
                ("iso_file", models.CharField(blank=True, max_length=255, null=True)),
                ("primary_mobile", models.CharField(max_length=255)),
                ("alternate_mobile", models.CharField(max_length=255)),
                ("account_name", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=255)),
                ("branch", models.CharField(max_length=255)),
                ("bank_name", models.CharField(max_length=255)),
                ("ifsc_code", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
