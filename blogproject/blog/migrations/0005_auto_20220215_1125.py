# Generated by Django 2.2.3 on 2022-02-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='expert',
            field=models.CharField(blank=True, max_length=200, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]