"""Unit test for the analysis module"""

import datetime as dt
import numpy as np

from floodsystem.analysis import polyfit


def test_polyfit_generates_a_polynomial_with_a_date_offset_of_the_first_date():

    initial_date = dt.datetime(2020, 1, 2, tzinfo=dt.timezone.utc)
    dates = [initial_date,
             initial_date + dt.timedelta(days=1),
             initial_date + dt.timedelta(days=2),
             initial_date + dt.timedelta(days=3),
             initial_date + dt.timedelta(days=4),
             initial_date + dt.timedelta(days=5)]

    expected_polynomial = np.poly1d([1, 2, 3, 4, 5])
    levels = [expected_polynomial(0),
              expected_polynomial(1),
              expected_polynomial(2),
              expected_polynomial(3),
              expected_polynomial(4),
              expected_polynomial(5)]

    poly, d0 = polyfit(dates, levels, 5)

    assert initial_date == d0
    assert expected_polynomial[0] == round(poly[0])
    assert expected_polynomial[1] == round(poly[1])
    assert expected_polynomial[2] == round(poly[2])
    assert expected_polynomial[3] == round(poly[3])
    assert expected_polynomial[4] == round(poly[4])
    assert expected_polynomial[5] == round(poly[5])


def test_polyfit_returns_false_if_the_dates_and_levels_arrays_are_not_the_same_length():

    initial_date = dt.datetime(2020, 1, 2, tzinfo=dt.timezone.utc)
    dates = [initial_date,
             initial_date + dt.timedelta(days=1),
             initial_date + dt.timedelta(days=2),
             initial_date + dt.timedelta(days=3),
             initial_date + dt.timedelta(days=4),
             initial_date + dt.timedelta(days=5)]

    polynomial = np.poly1d([1, 2, 3, 4, 5])
    levels = [polynomial(0),
              polynomial(1),
              polynomial(2),
              polynomial(3),
              polynomial(4)]

    poly, d0 = polyfit(dates, levels, 5)
    assert poly is False
    assert d0 is False
