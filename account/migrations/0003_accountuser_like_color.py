# Generated by Django 4.1.2 on 2023-06-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_accountuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='like_color',
            field=models.CharField(default='ui red', max_length=120),
        ),
    ]
