import pytest
from mockserver import MockServer


@pytest.fixture
def mockserver():
    return MockServer()
