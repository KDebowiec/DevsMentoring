import pytest
from calc_diff import *
import datetime


@pytest.fixture(autouse=True)
def mock_datetime_now(mocker):
    mock_datetime = datetime.datetime(2021, 11, 3, 9, 22, 28)
    mocker.patch.object(datetime, 'datetime', return_value=mock_datetime)


def test_calc_diff(mock_datetime_now):
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None  # None means that case is currently going on
    }

    assert calc_diff(case) == 0


# @pytest.fixture
# def mocking_datetime(mocker):
#    mocked_datetime_now = '2021-11-03T09:22:28+00:00'
#    mocker.patch('datetime.datetime.now', return_value=mocked_datetime_now)
#
#
# def test_if_calc_diff_returns_time(mocker):
#     case = {
#         'start_time': '2021-11-03T09:22:28+00:00',
#         'end_time': None  # None means that case is currently going on
#     }
#     mock_now = datetime(2021, 11, 3, 9, 22, 28)
#     mock_now_func = mocker.Mock(return_value=mock_now)
#
#     assert calc_diff(case) == 0
