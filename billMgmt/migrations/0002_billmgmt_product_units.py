# Generated by Django 4.2.5 on 2023-11-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billMgmt", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="billmgmt",
            name="product_units",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
