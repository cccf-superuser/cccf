# Generated by Django 4.2.5 on 2023-09-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]
