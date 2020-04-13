from django.db import models
from sispos.relatorios.models import Relatorios
from sispos.accounts.models import User
from uuid import uuid4

APROVADO = 'Aprovado'
REPROVADO = 'Reprovado'
STATUS_CHOICES = (('aprovado', APROVADO), ('reprovado', REPROVADO))


class Rds1(models.Model):
    desempenho = models.TextField('desempenho', max_length=2048)
    revisao = models.TextField('revisao', max_length=2048)
    definicao = models.TextField('definicao', max_length=2048)
    plano = models.TextField('planos', max_length=2048)
    resultados = models.TextField('resultados', max_length=2048)
    atividades = models.TextField('atividades', max_length=2048)
    relatorio = models.ForeignKey(Relatorios, on_delete=models.CASCADE)
    relator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField('status', max_length=12, choices=STATUS_CHOICES)
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)

    def get_absolute_url(self):
        return '/parecer/rds1/{}'.format(str(self.uuid))