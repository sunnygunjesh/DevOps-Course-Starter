import os
from _pytest import config
import pytest
import dotenv
from todo_app import app
from todo_app import trello_config
from todo_app.trello_config import TrelloConfig
from todo_app.trello_client import create_trello_board,delete_trello_board
from threading import Thread
from selenium import webdriver

@pytest.fixture(scope='module')
def app_with_temp_board(): 
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
   
    # Create the new board & update the board id environment variable
    board_id = create_trello_board(USE_A_REAL_INSTANCE_OF_TRELLO_CONFIG_HERE)
    os.environ['BOARD_ID'] = board_id

    # construct the new application    
    application = app.create_app()

    #start the app in its own thread.    
    thread = Thread(target=lambda: application.run(use_reloader=False))    
    thread.daemon = True    
    thread.start()    
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id,trello_config)