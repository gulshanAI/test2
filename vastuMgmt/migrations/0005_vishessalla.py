# Generated by Django 4.2.5 on 2023-09-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vastuMgmt", "0004_twod_threed_upay"),
    ]

    operations = [
        migrations.CreateModel(
            name="VishesSalla",
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
                ("vis_salla", models.TextField()),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
