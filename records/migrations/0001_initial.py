# Generated by Django 4.1.2 on 2022-11-02 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id_advisor', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
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
                ('id_author', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('curriculum_lattes', models.URLField()),
                ('google_scholar', models.URLField()),
                ('reasearch_gate', models.URLField()),
                ('linkedin', models.URLField()),
                ('orcid', models.URLField()),
                ('gitHub', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Co_advisor',
            fields=[
                ('id_co_advisor', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
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
                ('id_student', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
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
                ('id_monography', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('key_words', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('abstract', models.TextField(max_length=2500)),
                ('mography_link', models.URLField()),
                ('fk_advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orientador', to='records.advisor')),
                ('fk_co_advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_orientador', to='records.co_advisor')),
                ('fk_id_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='records.author')),
            ],
        ),
    ]
