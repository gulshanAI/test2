# Generated by Django 4.2.5 on 2023-09-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jyotishiMgmt", "0007_alter_jyotishisalla_jyo_salla_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jyotishisalla",
            name="jyo_salla",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="jyotishiupay",
            name="jyo_upay",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vishessalla",
            name="vis_salla",
            field=models.TextField(),
        ),
    ]