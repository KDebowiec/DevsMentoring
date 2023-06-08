from calc_diff import *
from datetime import datetime
def test_calc_diff(mocker):
    NOW = datetime(year=2021, month=11, day=3, hour=9, minute=22,  second=28, tzinfo=timezone.utc)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("calc_diff.datetime", mock_datetime)
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }
    assert calc_diff(case) == 0