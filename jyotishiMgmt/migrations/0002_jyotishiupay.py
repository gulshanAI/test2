# Generated by Django 4.2.5 on 2023-09-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jyotishiMgmt", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JyotishiUpay",
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
                ("jyo_upay", models.CharField(max_length=500)),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]