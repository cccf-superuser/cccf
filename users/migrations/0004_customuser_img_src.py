# Generated by Django 4.2.5 on 2023-09-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_admission_year_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img_src',
            field=models.URLField(blank=True, null=True),
        ),
    ]