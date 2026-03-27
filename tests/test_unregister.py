def test_unregister_successfully_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants?email={existing_email}"

    # Act
    response = client.delete(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 200
    assert result["message"] == f"Unregistered {existing_email} from {activity_name}"


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    endpoint = "/activities/Unknown%20Club/participants?email=student@mergington.edu"

    # Act
    response = client.delete(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 404
    assert result["detail"] == "Activity not found"


def test_unregister_returns_404_for_non_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email_not_registered = "notregistered@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants?email={email_not_registered}"

    # Act
    response = client.delete(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 404
    assert result["detail"] == f"{email_not_registered} is not signed up for {activity_name}"


def test_unregister_returns_422_when_email_is_missing(client):
    # Arrange
    endpoint = "/activities/Chess%20Club/participants"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 422
