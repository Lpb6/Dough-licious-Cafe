# Generated by Django 4.1 on 2024-04-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_originalglaze_flavor_originalglaze_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strawberry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('regular', 'Regular'), ('Donut Hole', 'Donut Hole')], max_length=20)),
                ('flavor', models.CharField(choices=[('Strawberry', 'Strawberry')], max_length=20)),
                ('image', models.ImageField(upload_to='starberry_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='originalglaze',
            name='size',
            field=models.CharField(choices=[('regular', 'Regular'), ('Donut Hole', 'Donut Hole')], max_length=20),
        ),
    ]
