# Generated by Django 3.1.7 on 2021-03-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210315_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancedetails',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='staffdbs',
            name='phonenumber',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='studentdbs',
            name='phonenumber',
            field=models.BigIntegerField(),
        ),
    ]