# Generated by Django 2.0.2 on 2018-07-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='target_partner',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
