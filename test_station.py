# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent_is_true_only_for_consistent_typical_ranges():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    trange = (-2.3, 3.4445)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.typical_range_consistent()

    trange = (2.3, -3.4445)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    s = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    assert not s.typical_range_consistent()


def test_inconsistent_typical_range_stations_returns_a_list_of_all_inconsistent_stations():
    stations = []

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    trange = (-2.3, 3.4445)
    stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))
    trange = (2.3, -3.4445)
    stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))
    trange = None
    stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    actual_inconsistent_stations = inconsistent_typical_range_stations(stations)
    expected_inconsistent_stations = [stations[1], stations[2]]
    assert expected_inconsistent_stations == actual_inconsistent_stations

def test_relative_water_level():

    stations = []

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    trange = (2.3, -3.4445)
    stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))
    trange = (2.0, -1.6211)
    stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    actual_relative_water_level = relative_water_level(stations)
    print(actual_relative_water_level)
   # assert expected_relative_water == actual_relative_water
