# Generated by Django 4.0.1 on 2022-05-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_postproperty_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postproperty',
            name='ower_name',
        ),
        migrations.AddField(
            model_name='postproperty',
            name='owner_name',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
