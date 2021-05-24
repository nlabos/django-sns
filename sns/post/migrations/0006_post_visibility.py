# Generated by Django 3.1.3 on 2021-05-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210522_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', '公開'), ('PRIVATE', '非公開')], default='PUBLIC', max_length=10),
        ),
    ]