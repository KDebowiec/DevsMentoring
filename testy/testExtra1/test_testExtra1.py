from unittest.mock import patch

import pytest
import testExtra1
from datetime import datetime


@pytest.fixture
def menu_instance(mocker):
    mocker.patch('builtins.input', return_value='5')
    return testExtra1.menu()

# @pytest.fixture
# def bus_depot_instance(mocker):
#    mock_depot = mocker.Mock(spec=testExtra1.BusDepot)
#    mock_depot.name = "bus_depot"
#    mock_depot.kind = "bus"
#    return mock_depot


@patch('testExtra1.BusDepot')
def test_add_bus(menu_instance, mocker):
    mocker.patch('testExtra1.list_of_depots', ['bus_depot'])
    mocker.patch('builtins.input', side_effect=[100, 10, 'bus_depot', 10])
    testExtra1.add_bus()
    assert len(testExtra1.list_of_vehicless) == 1


@patch('testExtra1.TramDepot')
def test_add_tram(menu_instance, mocker):
    mocker.patch('testExtra1.list_of_depots', ['tram_depot'])
    mocker.patch('builtins.input', side_effect=[100, 10, 'tram_depot', 10])
    testExtra1.add_tram()
    assert len(testExtra1.list_of_vehicless) == 2


def test_add_bus_depot(menu_instance, mocker):
    mocker.patch('testExtra1.list_of_depots', [])
    mocker.patch('builtins.input', side_effect=['bus_stop', 'zajezdnia autobusowa'])
    testExtra1.add_bus_depot()
    assert bus_stop in testExtra1.list_of_depots
#
# def test_add_tram_depot():
#     add_tram_depot()
#     assert len(list_of_depots) == 1
#     assert isinstance(list_of_depots[0], TramDepot)
#
# def test_show_vehicles(capfd):
#     add_bus()
#     add_tram()
#     add_bus_depot()
#     add_tram_depot()
#     show_vehicles()
#     output = capfd.readouterr()[0]
#     assert "tramwaj" in output
#     assert "bus" in output
#
