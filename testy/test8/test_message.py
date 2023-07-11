import pytest
from message import *


def test_show_message(mocker):
    mock_print = mocker.patch('builtins.print')
    show_message('hello')

    mock_print.assert_called_once_with('Your message: hello')
