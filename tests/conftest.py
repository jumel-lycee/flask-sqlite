import pytest

import main

@pytest.fixture
def app():
    app = main.app
    return app

@pytest.fixture
def client(app):
    return app.test_client()
