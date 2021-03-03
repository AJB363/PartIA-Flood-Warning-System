from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import towns_most_at_risk, stations_highest_rel_level, stations_level_over_threshold
from floodsystem.station import MonitoringStation


def test_towns_most_at_risk_returns_N_towns():

    exptected_length = 5
    stations = build_station_list()[:exptected_length * 5]
    update_water_levels(stations)

    towns = towns_most_at_risk(stations, exptected_length)
    assert len(towns) == exptected_length


def test_towns_most_at_risk_returns_towns_sorted_by_risk_level():

    exptected_length = 5
    stations = build_station_list()[:exptected_length * 5]
    update_water_levels(stations)

    towns = towns_most_at_risk(stations, exptected_length)
    for i in range(exptected_length - 1):
        assert towns[i][2] >= towns[i + 1][2]


def test_stations_level_over_threshold():

    test_tol = 0.5
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    trange = (0, 1)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = 0.9
    s2.latest_level = 0.4
    s3.latest_level = 1.5
    s4.latest_level = -1.0
    s5.latest_level = None
    stations = [s1, s2, s3, s4, s5]

    expected_stations = [s3, s1]
    actual_stations = stations_level_over_threshold(stations, test_tol)
    assert expected_stations == actual_stations


def test_stations_highest_rel_level():

    N = 3
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    trange1 = (1.1, 3.0)
    trange2 = (-1.2, 2.5)
    trange3 = (-1.67, 3.14)
    trange4 = (0, 1)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange4, river, town)
    s1.latest_level = 4.1
    s2.latest_level = 1.0
    s3.latest_level = 1.9
    s4.latest_level = None
    stations = [s1, s2, s3, s4]

    expected_stations_highest_rel_level = [s1, s3, s2]
    actual_stations_highest_rel_level = stations_highest_rel_level(stations, N)

    assert expected_stations_highest_rel_level == actual_stations_highest_rel_level
