import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_dashboard_requires_login(client):
    """
    Unauthenticated users should be redirected to login
    """

    response = client.get("/finance/")
    assert response.status_code == 302  # redirect


@pytest.mark.django_db
def test_dashboard_logged_in_user(client):
    """
    Logged-in users should access dashboard
    """

    user = User.objects.create_user(
        username="financeuser",
        password="securepass"
    )

    client.login(username="financeuser", password="securepass")

    response = client.get("/finance/")
    assert response.status_code == 200
