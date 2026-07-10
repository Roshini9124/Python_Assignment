from src.TimeDelta.util import time_delta


def test_sample_case_1():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == 25200


def test_sample_case_2():
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Fri 01 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == 88200


def test_same_timestamp():
    t1 = "Mon 01 Jan 2024 00:00:00 +0000"
    t2 = "Mon 01 Jan 2024 00:00:00 +0000"
    assert time_delta(t1, t2) == 0


def test_one_hour_difference():
    t1 = "Mon 01 Jan 2024 01:00:00 +0000"
    t2 = "Mon 01 Jan 2024 00:00:00 +0000"
    assert time_delta(t1, t2) == 3600


def test_timezone_difference():
    t1 = "Mon 01 Jan 2024 10:00:00 +0530"
    t2 = "Mon 01 Jan 2024 04:30:00 +0000"
    assert time_delta(t1, t2) == 0