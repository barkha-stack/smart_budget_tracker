import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_page_loads(client):
    """
    This test checks:
    - login page URL works
    - returns HTTP 200 (success)
    """

    url = reverse("login")  # Django built-in login view
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_login(client):
    """
    This test checks:
    - user can log in with valid credentials
    """

    # Create a test user (only exists in test DB)
    user = User.objects.create_user(
        username="testuser",
        password="testpass123"
    )

    login = client.login(
        username="testuser",
        password="testpass123"
    )

    assert login is True
