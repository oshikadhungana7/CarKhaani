# Generated by Django 3.0.4 on 2021-02-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0004_owner_owner_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='Owner_age',
        ),
        migrations.AddField(
            model_name='owner',
            name='Owner_gender',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='owner',
            name='Owner_license',
            field=models.ImageField(upload_to='img/Owner_License/'),
        ),
    ]