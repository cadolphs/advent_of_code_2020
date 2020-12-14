from day13.run_day13 import find_interval_with_smallest_wait_time_for, wait_time_for


def test_wait_time_for_example():
    assert 5 == wait_time_for(939, 59)


def test_find_smallest_wait_time():
    intervals = [7, 13, 59, 31, 19]

    assert 59, 5 == find_interval_with_smallest_wait_time_for(939, intervals)
