# Generated by Django 4.1.3 on 2023-04-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='fname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='gender',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='lname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
