# Generated by Django 2.1.4 on 2019-01-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qarchapp', '0006_information_introduction_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]