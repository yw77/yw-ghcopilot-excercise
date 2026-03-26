from src.app import activities


def test_get_activities_returns_activity_dictionary(client):
    # Arrange
    endpoint = "/activities"
    expected_count = len(activities)

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == expected_count


def test_get_activities_contains_expected_fields_per_activity(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for activity_details in payload.values():
        assert required_fields.issubset(activity_details.keys())
        assert isinstance(activity_details["participants"], list)
