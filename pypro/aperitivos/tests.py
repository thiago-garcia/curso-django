from django.urls import reverse
import pytest

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Vídeo Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp,
                    '<iframe src="https://player.vimeo.com/video/288344114?h=63fff44243&title=0&byline=0&portrait=0"')
