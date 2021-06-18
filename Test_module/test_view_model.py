from todo_app.view_model import ViewModel
from todo_app.todo_item import TodoItem

def test_viewmodel_todo_items():
    items = [
             TodoItem(1,"To Do", "This is for To do items"),
             TodoItem(2,"Doing", "This is for Doing items"),
             TodoItem(3,"Done", "This is for Done items")
            ]
    viewmodel = ViewModel(items)
    todoitems = viewmodel.todo_items

    assert len(todoitems) == 1
    item = todoitems[0]
    assert item.status == 'To Do'

def test_viewmodel_doing_items():
    items = [
              TodoItem(1,"To Do", "This is for Doing items"),
              TodoItem(2,"Doing", "This is for Doing items"),
              TodoItem(3,"Done", "This is for Done items")
            ]
    viewmodel = ViewModel(items)
    doingitems = viewmodel.doing_items

    assert len(doingitems) == 1
    item = doingitems[0]
    assert item.status == 'Doing'

def test_viewmodel_done_items():
    items = [
              TodoItem(1,"To Do", "This is for Doing items"),
              TodoItem(2,"Doing", "This is for Doing items"),
              TodoItem(3,"Done", "This is for Done items")
            ]
    viewmodel = ViewModel(items)
    doneitems = viewmodel.done_items

    assert len(doneitems) == 1
    item = doneitems[0]
    assert item.status == 'Done'