# Generated by Django 2.2.1 on 2019-06-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0006_auto_20190610_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
