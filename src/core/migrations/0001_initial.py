# Generated by Django 4.1 on 2022-11-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(max_length=300)),
                ('questions_en', models.TextField(max_length=300, null=True)),
                ('questions_ru', models.TextField(max_length=300, null=True)),
                ('answers', models.TextField(max_length=300)),
                ('answers_en', models.TextField(max_length=300, null=True)),
                ('answers_ru', models.TextField(max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faq',
            },
        ),
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('message_en', models.TextField(null=True)),
                ('message_ru', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'SendMessage',
                'verbose_name_plural': 'SendMessage',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Subscribers',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='src/static/workers_image')),
                ('position', models.CharField(max_length=20)),
                ('position_en', models.CharField(max_length=20, null=True)),
                ('position_ru', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Workers',
                'verbose_name_plural': 'Workers',
            },
        ),
    ]