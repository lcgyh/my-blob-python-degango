# Generated by Django 2.1.1 on 2018-09-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='我是标题', max_length=32)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
