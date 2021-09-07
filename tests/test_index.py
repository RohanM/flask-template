import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def index(client):
    rv = client.get('/')
    return BeautifulSoup(rv.data, 'html.parser')


def test_title(index):
    assert index.select('h2')[0].string == 'Site Title'
