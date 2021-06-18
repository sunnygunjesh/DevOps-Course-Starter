from unittest.mock import Mock, patch
from todo_app import app
import pytest
import os
#import dotenv
#import python-dotenv
from dotenv import find_dotenv, load_dotenv	
#load_dotenv(find_dotenv())

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app
    test_app = app.create_app()


    # Use the app to create a test_client
    with test_app.test_client() as client:
        yield client

def mock_get_lists(url, params):  
    sample_trello_lists_response = [
    {
        "id": "123400",
        "name": "Test1",
        "pos": 12345,
        "idList": os.getenv('TODO_LIST_ID')
    },   
    {
        "id": "123450",
        "name": "Testdoing",
        "pos": 12346,
        "idList": os.getenv('DOING_LIST_ID')
    },
    {
        "id": "123456",
        "name": "Testdone",
        "pos": 12347,
        "idList": os.getenv('DONE_LIST_ID')
    }
]
    board_id= os.getenv('BOARD_ID')
    if url == f"https://api.trello.com/1/boards/{board_id}/cards" : 
        
        response = Mock()
        response.status_code = 200
        response.json.return_value = sample_trello_lists_response
        return response
    return None

@patch('requests.get')
def test_index_page(mock_get_requests, client):

    mock_get_requests.side_effect = mock_get_lists
    
    response = client.get('/')

    assert response.status_code == 200
    assert b'Testdoing' in response.data
	

