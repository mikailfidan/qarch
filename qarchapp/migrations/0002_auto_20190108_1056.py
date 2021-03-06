# Generated by Django 2.1.4 on 2019-01-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qarchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name': 'İçerik', 'verbose_name_plural': 'İçerikler'},
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
