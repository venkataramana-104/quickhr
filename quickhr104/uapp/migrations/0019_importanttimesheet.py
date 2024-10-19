# Generated by Django 5.0.6 on 2024-09-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapp', '0018_createroster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Importanttimesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Template', models.CharField(choices=[('Template1', 'Template1'), ('Template2', 'Template2'), ('Template3', 'Template3')], max_length=10)),
                ('Format', models.CharField(choices=[('Excel', 'Excel'), ('CSV', 'CSV')], max_length=10)),
                ('Upload_Document', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
