from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: snapshot current in-memory data before each test.
    original_state = deepcopy(activities)

    yield

    # Assert/cleanup: restore shared state so tests remain independent.
    activities.clear()
    activities.update(original_state)
