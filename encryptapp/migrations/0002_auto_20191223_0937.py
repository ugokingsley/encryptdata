# Generated by Django 2.2.7 on 2019-12-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryptapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptdata',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
