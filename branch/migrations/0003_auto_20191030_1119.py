# Generated by Django 2.2.6 on 2019-10-30 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branch_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses.Courses'),
        ),
    ]
