# Generated by Django 5.0.6 on 2024-08-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapp', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='leavef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee', models.CharField(max_length=30)),
                ('Leavetype', models.CharField(max_length=302)),
                ('Balance_Leave', models.CharField(max_length=500)),
                ('From_Date', models.CharField(max_length=30)),
                ('To_Date', models.CharField(max_length=30)),
                ('Session', models.CharField(max_length=300)),
                ('No_ofdaysapplying', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=300)),
                ('Upload_Document', models.CharField(max_length=30)),
            ],
        ),
    ]
