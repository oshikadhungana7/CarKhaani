# Generated by Django 3.0.4 on 2021-01-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0003_customer_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
