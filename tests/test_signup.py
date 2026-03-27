def test_signup_successfully_registers_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    new_email = "newstudent@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup?email={new_email}"

    # Act
    response = client.post(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 200
    assert result["message"] == f"Signed up {new_email} for {activity_name}"


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    endpoint = "/activities/Unknown%20Club/signup?email=student@mergington.edu"

    # Act
    response = client.post(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 404
    assert result["detail"] == "Activity not found"


def test_signup_returns_409_for_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    endpoint = f"/activities/{activity_name}/signup?email={existing_email}"

    # Act
    response = client.post(endpoint)
    result = response.json()

    # Assert
    assert response.status_code == 409
    assert result["detail"] == f"{existing_email} is already signed up for {activity_name}"


def test_signup_returns_422_when_email_is_missing(client):
    # Arrange
    endpoint = "/activities/Chess%20Club/signup"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 422
