# Generated by Django 5.1 on 2024-11-30 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cadastro_colaboradores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_colaboradores',
            name='matricula',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Acoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEmprestimo', models.DateField()),
                ('dataDevolucao', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('condicoes', models.CharField(max_length=100)),
                ('dataDevolucaoReal', models.DateField(blank=True, null=True)),
                ('observacoes', models.TextField()),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cadastro_colaboradores')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipamentos')),
            ],
        ),
    ]
