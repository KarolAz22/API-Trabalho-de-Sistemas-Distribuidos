# Generated by Django 4.1.1 on 2022-10-01 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advirsor',
            fields=[
                ('id_advisor', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('curriculum_lattes', models.URLField()),
                ('google_scholar', models.URLField()),
                ('reasearch_gate', models.URLField()),
                ('linkedin', models.URLField()),
                ('orcid', models.URLField()),
                ('gitHub', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('curriculum_lattes', models.URLField()),
                ('google_scholar', models.URLField()),
                ('reasearch_gate', models.URLField()),
                ('linkedin', models.URLField()),
                ('orcid', models.URLField()),
                ('gitHub', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Co_advirsor',
            fields=[
                ('id_co_advisor', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('curriculum_lattes', models.URLField()),
                ('google_scholar', models.URLField()),
                ('reasearch_gate', models.URLField()),
                ('linkedin', models.URLField()),
                ('orcid', models.URLField()),
                ('gitHub', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_student', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('curriculum_lattes', models.URLField()),
                ('google_scholar', models.URLField()),
                ('reasearch_gate', models.URLField()),
                ('linkedin', models.URLField()),
                ('orcid', models.URLField()),
                ('gitHub', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Monograph',
            fields=[
                ('id_monography', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('key_words', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('abstract', models.CharField(max_length=255)),
                ('mography_link', models.URLField()),
                ('fk_advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.advirsor')),
                ('fk_co_advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.co_advirsor')),
                ('fk_id_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.author')),
            ],
        ),
    ]
