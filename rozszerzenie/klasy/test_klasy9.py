import pytest
import klasy9
from datetime import datetime

@pytest.fixture
def tanks_instance(mocker):
    mocker.patch('builtins.input', return_value='8')
    return klasy9.Tanks()

@pytest.fixture()
def tanks_all_operations(mocker):
    mocker.patch('builtins.input', return_value='9')
    return klasy9.Tanks()


def test_add_tank(tanks_instance, mocker):
    mocker.patch('klasy9.EVENT_LOG', [])
    mocker.patch('builtins.input', side_effect=['karol', '1000', '500'])
    NOW = datetime(year=2021, month=11, day=3, hour=9, minute=22,  second=28)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("klasy9.datetime", mock_datetime)
    tanks_instance.add_tank()
    assert tanks_instance.tank_dict['karol']['capacity'] == 1000
    assert tanks_instance.tank_dict['karol']['volume'] == 500
    assert len(klasy9.EVENT_LOG) == 1
    assert klasy9.EVENT_LOG[0]['karol']['time'] == NOW
    assert klasy9.EVENT_LOG[0]['karol']['operation_name'] == 'add_tank'
    assert klasy9.EVENT_LOG[0]['karol']['ilość wody'] == 500
    assert klasy9.EVENT_LOG[0]['karol']['succes'] == True

def test_check_volume_if_incorrect(tanks_instance):
    with pytest.raises(Exception):
        tanks_instance.check_volume(600, 500)


def test_pour_water(tanks_instance, mocker):
    mocker.patch('builtins.input', side_effect=['zbiornik1', 100])
    tanks_instance.pour_water()
    assert tanks_instance.tank_dict['zbiornik1']['volume'] == 900


def test_pour_out_water(tanks_instance, mocker):
    mocker.patch('builtins.input', side_effect=['zbiornik2', 100])
    tanks_instance.pour_out_water()
    assert tanks_instance.tank_dict['zbiornik2']['volume'] == 200


def test_transfer_water(tanks_instance, mocker):
    mocker.patch('klasy9.EVENT_LOG', [])
    mocker.patch('builtins.input', side_effect=['zbiornik1', 'zbiornik2', 100])
    NOW = datetime(year=2021, month=11, day=3, hour=9, minute=22, second=28)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("klasy9.datetime", mock_datetime)
    tanks_instance.transfer_water()
    assert len(klasy9.EVENT_LOG) == 2

def test_tank_with_most_water(tanks_instance):
    assert 'zbiornik3 ma najwięcej wody'


def test_fullest_tank(tanks_instance):
    assert 'zbiornik3 jest najpełniejszy'


def test_all_empty_tanks(tanks_instance):
    assert not tanks_instance.all_empty_tanks()


def test_show_events_all(tanks_instance, mocker, capsys):
    mocker.patch('builtins.input', side_effect=[1, 'zbiornik1'])
    tanks_instance.show_events()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'typ operacji: dolewanie wody do zbiornika\n'\
                                   'data i czas: 12, ilość wody: 400, \n'\
                                   'operacja zakończona sukcesem\n'\
                                   'typ operacji: dolewanie wody do zbiornika\n'\
                                   'data i czas: 12, ilość wody: 400, \n'\
                                   'operacja nieudana\n'\

