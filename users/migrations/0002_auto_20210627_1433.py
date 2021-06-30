# Generated by Django 3.0.5 on 2021-06-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refreshtoken',
            name='token',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(),
        ),
    ]
