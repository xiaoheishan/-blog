# Generated by Django 2.2.2 on 2019-06-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aritical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('center', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
