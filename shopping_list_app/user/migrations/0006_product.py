# Generated by Django 4.1.7 on 2023-03-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_shopping_list_price_alter_shopping_list_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('shopping_lists', models.ManyToManyField(to='user.shopping_list')),
            ],
        ),
    ]
