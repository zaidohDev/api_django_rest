# Generated by Django 2.1.1 on 2018-09-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('categories', models.ManyToManyField(to='api.Category')),
            ],
        ),
    ]