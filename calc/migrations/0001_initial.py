# Generated by Django 5.1 on 2024-08-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('age', models.CharField(max_length=300, null=True)),
                ('height', models.CharField(max_length=300, null=True)),
                ('weight', models.CharField(max_length=300, null=True)),
                ('DOB', models.DateField(max_length=300, null=True)),
                ('date', models.DateTimeField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('category', models.CharField(choices=[('Weightloss', 'Weightloss'), ('Weightgain', 'Weightgain'), ('Get-fit', 'Getfit'), ('lifestyle', 'lifestyle'), ('Recovery', 'Recovery')], max_length=300)),
                ('tags', models.ManyToManyField(to='calc.type')),
            ],
        ),
    ]
