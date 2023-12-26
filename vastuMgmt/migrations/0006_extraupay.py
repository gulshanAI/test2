# Generated by Django 4.2.5 on 2023-09-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vastuMgmt", "0005_vishessalla"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtraUpay",
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
                ("ext_upay", models.TextField()),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]