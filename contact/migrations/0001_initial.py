# Generated by Django 2.2.6 on 2019-10-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')])),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]