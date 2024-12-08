import requests
from unittest.mock import MagicMock
import pytest

def test_invalid_login(mocked_requests):
    url = "http://127.0.0.1:5500/teton/users"
    params = {"username": "admin", "password": "admin"}
    
    # Create a mock response object with the status_code and text attributes
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.text = ""
    
    # Set the mock to return the mock response when requests.get() is called
    mocked_requests.return_value = mock_response
    
    # Send a GET request with parameters
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code is 401 (Unauthorized)
    assert response.status_code == 401
    
    # Assert the response body is empty or plain text
    assert response.text.strip() == ""

def test_valid_login(mocked_requests):
    url = "http://127.0.0.1:5500/users"
    params = {"username": "admin", "password": "qwerty"}
    
    # Create a mock response object with the status_code and text attributes
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = ""
    
    # Set the mock to return the mock response when requests.get() is called
    mocked_requests.return_value = mock_response
    
    # Send a GET request with parameters
    response = requests.get(url, params=params)
    
    # Assert the HTTP status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert the response body is empty or plain text
    assert response.text.strip() == ""

# Use pytest-mock or unittest.mock to mock the requests library
@pytest.fixture
def mocked_requests(mocker):
    return mocker.patch('requests.get')
