import pytest
from src import *

def test_check_exceptions_in_check_pos_length():
    with pytest.raises(Exception):
        check_pos(-1, [])


def test_check_exceptions_in_check_pos_():
    with pytest.raises(Exception):
        check_pos(-1, [])


def test_add_todo_if_adds_element():
    # todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    old_length = len(todos)
    add_todo('something')
    new_length = len(todos)
    assert old_length < new_length


def test_remove_todo_if_removes_element():
    # todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    old_length = len(todos)
    remove_todo(1)
    new_length = len(todos)
    assert old_length > new_length


def test_if_method_edit_todo_edits_element():
    # todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    element = todos[1]
    edit_todo(1, 'new content')
    assert element != 'new content'


def test_if_remove_all_removes_all():
    # todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
    remove_all()
    assert len(todos) == 0