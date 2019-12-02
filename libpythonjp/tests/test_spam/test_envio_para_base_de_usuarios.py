from unittest.mock import Mock

import pytest

from libpythonjp.spam.main import EnviadorDeSpam
from libpythonjp.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jlplautz', email='jorge.plautz@gmail.com'),
            Usuario(nome='Linda', email='lindalene.plautz@gmail.com')
        ],
        [
            Usuario(nome='Jlplautz', email='jorge.plautz@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jorge.plautz@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jlplautz', email='jorge.plautz@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lindalene.plautz@gmail.com',  # remetente
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'lindalene.plautz@gmail.com',     # remetente
        'jorge.plautz@gmail.com',         # destinatario
        'Curso Python Pro',               # assunto
        'Confira os modulos fantasticos'  # corpo
    )
