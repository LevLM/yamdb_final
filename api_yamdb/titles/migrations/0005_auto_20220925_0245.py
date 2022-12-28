# Generated by Django 2.2.16 on 2022-09-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_auto_20220924_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-year',), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
