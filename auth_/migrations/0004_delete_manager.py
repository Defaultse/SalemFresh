# Generated by Django 3.1.7 on 2021-05-15 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth_', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
    ]