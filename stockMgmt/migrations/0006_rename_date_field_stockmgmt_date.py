# Generated by Django 4.2.5 on 2023-10-22 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stockMgmt", "0005_rename_dealer_mobile_stockmgmt_dealer_mob_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stockmgmt",
            old_name="date_field",
            new_name="date",
        ),
    ]