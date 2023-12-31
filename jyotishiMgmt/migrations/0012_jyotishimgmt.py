# Generated by Django 4.2.5 on 2023-09-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jyotishiMgmt", "0011_rename_karmicupay_karmikupay"),
    ]

    operations = [
        migrations.CreateModel(
            name="JyotishiMgmt",
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
                ("client_id", models.IntegerField()),
                ("date_field", models.DateField()),
                ("jyo_questions", models.CharField(max_length=500)),
                ("jyo_upay", models.TextField()),
                ("jyo_salla", models.TextField()),
                ("vis_salla", models.TextField()),
                ("kar_upay", models.TextField()),
                ("a_id", models.IntegerField(blank=True, null=True)),
                ("delete", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
