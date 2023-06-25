import pytest
import main
from main import *


@pytest.fixture
def menu_instance(mocker):
    mocker.patch('builtins.input', return_value='6')
    return main.Menu()


def test_rot13_encrypt(menu_instance, mocker):
    mocker.patch('builtins.input', side_effect=['Hello', 'rot13'])
    menu_instance.encrypt_text()
    assert menu_instance.encrypted_words['text']  == 'Uryyb'

def test_rot47_encrypt(menu_instance, mocker):
    mocker.patch('builtins.input', side_effect=['Hello', 'rot47'])
    menu_instance.encrypt_text()
    assert menu_instance.encrypted_words['text']  == 'w6==@'

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello", "Hello")])
def test_input_reader_read_input_valid(input_text, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_text)
    result = InputReader.read_input("Enter input: ")
    assert result == expected_output


@pytest.mark.parametrize("input_text, expected_output", [("ą bc", "bc")])
def test_input_reader_read_input_invalid(input_text, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_text)

    with pytest.raises(ValueError) as exc_info:
        InputReader.validate_input(input_text)

    assert str(exc_info.value) == f"Invalid character 'ą' found in input."