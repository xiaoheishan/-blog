# Generated by Django 2.2.2 on 2019-06-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_aritical_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aritical',
            old_name='center',
            new_name='centent',
        ),
        migrations.AddField(
            model_name='aritical',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
    ]
