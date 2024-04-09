from django.urls import reverse
import pytest

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Vídeo Aperitivo: Motivação',
        'Instalação Windows',
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


# def test_conteudo_video(resp):
#     assert_contains(resp,
#                     '<iframe src="https://player.vimeo.com/video/288344114"')
