import os
from _pytest import config
import time
import pytest
import dotenv
from todo_app import app
from todo_app import trello_config
from todo_app.trello_config import TrelloConfig
from todo_app.trello_client import create_trello_board,delete_trello_board,get_todo_lists_on_board,get_doing_lists_on_board,get_done_lists_on_board
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

@pytest.fixture(scope='module')
def app_with_temp_board(): 
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    trloconfig = TrelloConfig()

    # Create the new board & update the board id environment variable
    board_id = create_trello_board(trloconfig)
    os.environ['BOARD_ID'] = board_id

    trloconfig = TrelloConfig()
    todo_list_id = get_todo_lists_on_board(board_id,trloconfig)
    os.environ['TODO_LIST_ID'] = todo_list_id
    
    trloconfig = TrelloConfig()
    doing_list_id = get_doing_lists_on_board(board_id,trloconfig)
    os.environ['DOING_LIST_ID'] = doing_list_id
    
    trloconfig = TrelloConfig()
    done_list_id = get_done_lists_on_board(board_id,trloconfig)
    os.environ['DONE_LIST_ID'] = done_list_id

    # construct the new application    
    application = app.create_app()

    #start the app in its own thread.    
    thread = Thread(target=lambda: application.run(use_reloader=False))    
    thread.daemon = True    
    thread.start()    
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id,trloconfig)

@pytest.fixture(scope="module")
def driver():  

    with webdriver.Firefox() as driver:
            yield driver

def test_task_journey(driver: webdriver, app_with_temp_board):   
    driver.get('http://localhost:5000/') 
    #text_box: WebElement = driver.find_element_by_name('title')
    text_box: WebElement = WebDriverWait(driver, timeout=5).until(lambda d:
    d.find_element_by_name('title'))
    text_box.send_keys("Test Todo")
    submit_button: WebElement = WebDriverWait(driver, timeout=5).until(lambda d:
    d.find_element_by_name('submit'))
    submit_button.click()
    doing_button: WebElement = WebDriverWait(driver, timeout=5).until(lambda d:
    d.find_element_by_name('doing-button'))
    doing_button.click()
    done_button: WebElement = WebDriverWait(driver, timeout=5).until(lambda d:
    d.find_element_by_name('done-button'))
    done_button.click()
    item_text: WebElement = WebDriverWait(driver, timeout=5).until(lambda d:
    d.find_element_by_name('item-text'))
    assert item_text.text == 'Test Todo - Done'    