# Generated by Django 4.2.5 on 2023-10-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "vastuMgmt",
            "0013_remove_vastumgmt_badal_disha_remove_vastumgmt_disha_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="vastumgmt",
            name="bsn_upay_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="etar_upay_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="ext_upay_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="parinam_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="twod_threed_upay_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="vis_salla_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="vastumgmt",
            name="vis_upay_id",
            field=models.TextField(),
        ),
    ]
