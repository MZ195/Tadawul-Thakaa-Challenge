# Generated by Django 2.2.4 on 2021-08-02 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0003_auto_20210802_2312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dividendindustryaverage',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='dividendindustryaverage',
            table='dividend_Industry_Average',
        ),
    ]