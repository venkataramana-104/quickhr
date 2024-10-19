# Generated by Django 5.0.6 on 2024-08-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapp', '0004_addnewemployees'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=30)),
                ('claim_type', models.CharField(max_length=302)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('project', models.CharField(max_length=500)),
                ('custom_claim', models.CharField(max_length=500)),
                ('receipt_id', models.CharField(max_length=500)),
                ('attachment1', models.FileField(blank=True, null=True, upload_to='employee_documents/')),
                ('attachment2', models.FileField(blank=True, null=True, upload_to='employee_documents/')),
                ('description', models.TextField(max_length=600)),
            ],
        ),
    ]
