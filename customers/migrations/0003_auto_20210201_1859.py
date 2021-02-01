# Generated by Django 3.0.5 on 2021-02-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210201_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='firstName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='lastName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
