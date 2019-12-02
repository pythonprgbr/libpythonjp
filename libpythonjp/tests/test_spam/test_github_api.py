from unittest.mock import Mock

import pytest

from libpythonjp import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jlplautz')
    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/30046706?v=4'
    resp_mock.json.return_value = {
        'login': 'jlplautz', 'id': 30046706,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonjp.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('jlplautz')
    assert 'https://avatars1.githubusercontent.com/u/30046706?v=4' == url
