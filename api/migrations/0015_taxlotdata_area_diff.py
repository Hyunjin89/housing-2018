# Generated by Django 2.0.1 on 2018-06-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180613_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxlotdata',
            name='area_diff',
            field=models.IntegerField(null=True),
        ),
    ]
