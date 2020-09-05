from django.forms import ModelForm
from .models import Transacao


class TransacaoForm(ModelForm):
    # meta classe redefine variaveis da classe principal
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
