import pytest
from testExtra1 import *


def test_add_bus():
    add_bus()
    assert len(list_of_vehicless) == 1
    assert isinstance(list_of_vehicless[0], Bus)

def test_add_tram():
    add_tram()
    assert len(list_of_vehicless) == 1
    assert isinstance(list_of_vehicless[0], Tram)

def test_add_bus_depot():
    add_bus_depot()
    assert len(list_of_depots) == 1
    assert isinstance(list_of_depots[0], BusDepot)

def test_add_tram_depot():
    add_tram_depot()
    assert len(list_of_depots) == 1
    assert isinstance(list_of_depots[0], TramDepot)

def test_show_vehicles(capfd):
    add_bus()
    add_tram()
    add_bus_depot()
    add_tram_depot()
    show_vehicles()
    output = capfd.readouterr()[0]
    assert "tramwaj" in output
    assert "bus" in output

