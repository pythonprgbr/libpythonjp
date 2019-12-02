from libpythonjp.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Jlplautz', email='jorge.plautz@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Jlplautz', email='jorge.plautz@gmail.com'),
        Usuario(nome='Linda', email='lindalene.plautz@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
