# Generated by Django 5.1.2 on 2024-10-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_lesson_options_course_timestamp_course_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='public_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]