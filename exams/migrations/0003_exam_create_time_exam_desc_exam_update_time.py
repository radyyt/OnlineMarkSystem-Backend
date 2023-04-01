# Generated by Django 4.1.7 on 2023-04-01 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_alter_exam_author_examquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='desc',
            field=models.CharField(default='description', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
