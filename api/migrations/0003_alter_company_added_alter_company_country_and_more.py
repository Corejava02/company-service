# Generated by Django 4.2.4 on 2023-09-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_company_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='added',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='end_year',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='impact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='insight',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='intensity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='likelihood',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='pestle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='published',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='region',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='relevance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='sector',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='source',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='start_year',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='topic',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
