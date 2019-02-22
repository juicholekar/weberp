# Generated by Django 2.1.5 on 2019-02-13 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rawitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=10)),
                ('rate', models.PositiveIntegerField(blank=True, max_length=254)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]