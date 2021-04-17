# Generated by Django 3.1.7 on 2021-04-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.SmallIntegerField(choices=[(1, 'user'), (2, 'customer'), (3, 'shop owner'), (4, 'delivery guy'), (5, 'admin')], default=1),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
