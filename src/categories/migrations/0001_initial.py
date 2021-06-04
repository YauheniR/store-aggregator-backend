# Generated by Django 3.2.4 on 2021-06-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('position', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('position', 'name'),
            },
        ),
        migrations.CreateModel(
            name='ProviderCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categorymodel')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.providermodel')),
            ],
            options={
                'verbose_name': 'Provider Category',
                'verbose_name_plural': 'Provider Categories',
            },
        ),
    ]
