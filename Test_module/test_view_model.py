from todo_app.view_model import Viewmodel
from todo_app.todo_item import TodoItem

def test_viewmodel_todo_items():
    items = [
             TodoItem(1,"To Do", "This is for To do items"),
             TodoItem(2,"Doing", "This is for Doing items"),
             TodoItem(3,"Done", "This is for Done items")
            ]
    viewmodel = Viewmodel(items)
    todoitems = viewmodel.todo_items

    assert len(todoitems) == 1
    item = todoitems[0]
    assert item.status == 'To Do'

def test_viewmodel_doing_items():
    items = [
              TodoItem(1, "This is for Doing items","Doing")
            ]
    doingitems = Viewmodel.doing_items
    assert doingitems

def test_viewmodel_done_items():
    items = [
              TodoItem(1, "This is for Done items","Done")
            ]
    doneitems = Viewmodel.done_items
    assert doneitems
