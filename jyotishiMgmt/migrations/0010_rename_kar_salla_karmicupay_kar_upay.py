# Generated by Django 4.2.5 on 2023-09-16 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jyotishiMgmt", "0009_karmicupay"),
    ]

    operations = [
        migrations.RenameField(
            model_name="karmicupay",
            old_name="kar_salla",
            new_name="kar_upay",
        ),
    ]
