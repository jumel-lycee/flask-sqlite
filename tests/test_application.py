import pytest

def test_index(client):
    response = client.get('/')
    assert b"new" in response.data
