import pytest

from libpythonjp.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario',
                         ['jorge.plautz@gmail.com', 'lindalene.plautz@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['jorge.plautz@gmail.com', 'lindalene.plautz@gmail.com']

    for destinatario in destinatarios:
        resultado = enviador.enviar(
            destinatario,
            'lindalene.plautz@gmail.com',
            'Curso Python Pro',
            'Turma Bruno Rocha aberta.'
        )
        assert destinatario in resultado


@pytest.mark.parametrize('remetente',
                         ['', 'lindalene'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lindalene.plautz@gmail.com',
            'Curso Python Pro',
            'Turma Bruno Rocha aberta.'
        )
