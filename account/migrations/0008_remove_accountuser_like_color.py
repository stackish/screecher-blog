# Generated by Django 4.1.2 on 2023-06-10 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_accountuser_like_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountuser',
            name='like_color',
        ),
    ]
