# Generated by Django 3.2.3 on 2021-06-01 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20210531_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providercategorymodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categorymodel'),
        ),
    ]
