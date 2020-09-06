# Generated by Django 3.1 on 2020-09-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeManagement', '0016_auto_20200906_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='day',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='worked_hours',
            field=models.CharField(max_length=3),
        ),
    ]
