# Generated by Django 2.2.2 on 2019-06-17 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hscms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='avaImg',
            new_name='avaimg',
        ),
    ]