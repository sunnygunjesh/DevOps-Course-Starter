from flask import Flask, app,render_template, redirect, request
from todo_app import trello_config

import todo_app.trello_client as trello
from todo_app.view_model import ViewModel
from todo_app.todo_item import TodoItem
from todo_app.trello_config import TrelloConfig

def create_app():
    app = Flask(__name__)
    trello_config = TrelloConfig()

    @app.route('/')
    def index():
        raw_trello_cards = trello.get_cards(trello_config)
        items = [TodoItem.from_raw_trello_card(card) for card in raw_trello_cards]
        item_view_model = ViewModel(items)
        return  render_template('index.html',view_model=item_view_model)

    @app.route('/item/add', methods=['POST'])
    def add_item():
        name = request.form['title']
        trello.add_card(name,trello_config)
        return redirect("/")

    @app.route('/item/<id>/doing')
    def move_item_to_doing(id):
    #    trello.move_card_doing(id)
        trello.move_to_doing_card(id,trello_config)
        return redirect('/')

    @app.route('/item/<id>/done')
    def move_item_to_done(id):
    #    trello.move_card_done(id)
        trello.move_to_done_card(id,trello_config)
        return redirect('/')

    @app.route('/item/<id>/undo')
    def undo_card_move(id):
    #    trello.undo_card_movement(id)
        trello.undo_done_card(id,trello_config)
        return redirect('/')

    return app
