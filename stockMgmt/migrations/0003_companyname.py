# Generated by Django 4.2.5 on 2023-10-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stockMgmt", "0002_productname"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyName",
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
                ("company_name", models.TextField()),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]