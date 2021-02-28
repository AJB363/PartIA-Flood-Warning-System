"""Unit test for the plot module"""

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
from datetime import datetime as dt


def test_plot_water_levels_does_not_crash_if_levels_and_dates_are_not_the_same_length():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    dates = [dt(2025, 4, 3, 2, 1, 0),
             dt(2025, 4, 3, 2, 1, 1),
             dt(2025, 4, 3, 2, 1, 2),
             dt(2025, 4, 3, 2, 1, 3),
             dt(2025, 4, 3, 2, 1, 4)]
    levels = [0, 1, 2, 3, 4, 5]
    plot_water_levels(station, dates, levels)


def test_plot_water_level_with_fit_does_not_crash_if_levels_and_dates_are_not_the_same_length():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    dates = [dt(2025, 4, 3, 2, 1, 0),
             dt(2025, 4, 3, 2, 1, 1),
             dt(2025, 4, 3, 2, 1, 2),
             dt(2025, 4, 3, 2, 1, 3),
             dt(2025, 4, 3, 2, 1, 4)]
    levels = [0, 1, 2, 3, 4, 5]
    plot_water_level_with_fit(station, dates, levels, 4)
