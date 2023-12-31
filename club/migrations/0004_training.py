# Generated by Django 4.1.2 on 2023-09-12 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_list_opps_des_time22_list_opps_intern_time3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title7', models.CharField(max_length=40)),
                ('description7', models.CharField(max_length=2000)),
                ('short_des7', models.CharField(max_length=2000)),
                ('url_opp7', models.CharField(max_length=5000)),
                ('time7', models.CharField(max_length=50)),
                ('img7', models.ImageField(blank=True, null=True, upload_to='imagesopps')),
                ('category7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category7', to='club.category')),
            ],
        ),
    ]
