# Generated by Django 4.1.1 on 2022-09-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooks',
            name='Genre',
            field=models.CharField(choices=[('Fantasy', 'Fantasy'), ('Literary', 'Literary'), ('Mystery', 'Mystery'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller')], max_length=15),
        ),
    ]
