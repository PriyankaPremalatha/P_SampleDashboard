# Generated by Django 3.0.3 on 2020-03-06 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgInsertion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TicketRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
                ('prioritylevel', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=12)),
                ('summary', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('assignee', models.CharField(blank=True, max_length=150)),
                ('duedate', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('priority', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('Related', models.CharField(max_length=150)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status1', models.CharField(blank=True, max_length=100)),
                ('status2', models.CharField(blank=True, max_length=100)),
                ('creator', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]