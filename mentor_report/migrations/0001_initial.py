# Generated by Django 5.0.4 on 2024-05-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentor_tb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=255)),
                ('m_dept', models.CharField(max_length=255)),
                ('m_batch', models.IntegerField()),
                ('m_students', models.IntegerField()),
            ],
        ),
    ]
