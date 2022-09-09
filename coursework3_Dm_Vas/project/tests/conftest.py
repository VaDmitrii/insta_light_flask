import pytest

from ..run import app


@pytest.fixture()
def test_client():
    return app.test_client()
