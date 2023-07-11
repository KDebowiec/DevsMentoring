import pytest
import main


@pytest.fixture
def menu_instance(mocker):
    mocker.patch('builtins.input', return_value='6')
    return main.Menu()


@pytest.fixture
def mock_open(mocker):
    def _mock_open(file_content):
        mock_file = mocker.mock_open(read_data=file_content)
        mocker.patch("builtins.open", mock_file)
        return mock_file

    return _mock_open


def test_rot13_encrypt(menu_instance, mocker):
    mocker.patch('builtins.input', side_effect=['Hello', 'rot13'])
    menu_instance.encrypt_text()
    assert menu_instance.encrypted_words['text'] == 'Uryyb'


def test_rot47_encrypt(menu_instance, mocker):
    mocker.patch('builtins.input', side_effect=['Hello', 'rot47'])
    menu_instance.encrypt_text()
    assert menu_instance.encrypted_words['text'] == 'w6==@'


def test_saving_to_file(menu_instance, mocker, tmp_path):
    menu_instance.encrypted_words = {'code': 'rot13', 'text': 'testing'}
    file_path = tmp_path / 'encrypted_texts.txt'
    item = f'typ kodowania: {menu_instance.encrypted_words["code"]},tekst: {menu_instance.encrypted_words["text"]}\n'
    menu_instance.file_handler.save_to_file(file_path, item)
    expected = 'typ kodowania: rot13,tekst: testing\n'


    with open(file_path, 'r') as file:
        data = file.readlines()
        print(data)
    assert expected in data


def test_decrypting_from_file_rot13(menu_instance, mocker, mock_open):
    file_content = 'typ kodowania: rot13,tekst: uryyb\n'
    mock_file = mock_open(file_content)
    menu_instance.decrypt_from_file()
    assert menu_instance.decrypted_text == 'hello'


def test_printing_from_file(menu_instance, mocker, tmp_path, mock_open, capsys):
    file_content = 'typ kodowania: rot13,tekst: uryyb\n'
    mock_file = mock_open(file_content)
    menu_instance.printing_file()
    captured = capsys.readouterr()
    x = captured.out.strip()
    assert x == 'typ kodowania: rot13,tekst: uryyb'


def test_decrypting_from_file_rot47(menu_instance, mocker, tmp_path, mock_open):
    file_content = 'typ kodowania: rot47,tekst: 96==@\n'
    mock_file = mock_open(file_content)
    menu_instance.decrypt_from_file()
    assert menu_instance.decrypted_text == 'hello'


def test_printing_words_from_memory(menu_instance, mocker, capsys):
    menu_instance.encrypted_words = {'code': 'rot13', 'text': 'testing'}
    menu_instance.print_encrypted_words()
    captured = capsys.readouterr()
    x = captured.out.strip()
    assert x == 'typ kodowania: rot13,tekst: testing'


@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello", "Hello")])
def test_input_reader_read_input_valid(input_text, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_text)
    result = main.InputReader.read_input("Enter input: ")
    assert result == expected_output


@pytest.mark.parametrize("input_text, expected_output", [("ą bc", "bc")])
def test_input_reader_read_input_invalid(input_text, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_text)

    with pytest.raises(ValueError) as exc_info:
        main.InputReader.validate_input(input_text)

    assert str(exc_info.value) == f"Invalid character 'ą' found in input."