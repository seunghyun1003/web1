# Generated by Django 2.2.6 on 2019-12-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simp_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='글의 분뉴를 입력하세요.(ex: 간단한 메모)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_image', models.ImageField(blank=True, upload_to='')),
                ('content', models.TextField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(help_text='글의 분류를 설정하세요.', to='simp_web.Category')),
            ],
        ),
    ]