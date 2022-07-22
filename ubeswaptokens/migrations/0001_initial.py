# Generated by Django 4.0.6 on 2022-07-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UbeswapModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubetokenlogourl', models.URLField(max_length=1000)),
                ('ubetokenname', models.CharField(max_length=1000)),
                ('uberewards', models.FloatField()),
                ('ubeprice', models.FloatField()),
            ],
        ),
    ]