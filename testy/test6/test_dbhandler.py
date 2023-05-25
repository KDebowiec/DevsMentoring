import pytest
from dbhandler import *


@pytest.fixture
def set_config_values(mocker):
    mocker.patch('decouple.config', return_value='MOCKED_VALUE')


def test_connect_to_database_should_return_expected_str_when_connectedToDb(set_config_values):
    from dbhandler import DbHandler
    actual = DbHandler().connect_to_database()
    expected = 'I am connecting to MOCKED_VALUE as MOCKED_VALUE with pass: MOCKED_VALUE...'
    assert actual == expected
