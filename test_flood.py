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

    test_tol = 0.7
    test_stations1 = []
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    trange1 = (1.1, 3.0)
    trange2 = (-1.2, 2.5)
    trange3 = (-1.67, 3.14)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    test_stations2 = [s1, s2, s3]

    for station in test_stations2:
        if station.relative_water_level() > test_tol:
            test_stations1.append((station.name, station.relative_water_level()))

    expected_level_over_threshold = sorted(test_stations1, key=lambda x: x[1], reverse=True)
    actual_level_over_threshold = stations_level_over_threshold(test_stations2, test_tol)
    assert expected_level_over_threshold == actual_level_over_threshold


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
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    test_stations = [s1, s2, s3]

    assert s1.relative_water_level() is not None
    assert s2.relative_water_level() is not None
    assert s3.relative_water_level() is not None

    expected_stations_highest_rel_level = []
    for station in test_stations:
        expected_stations_highest_rel_level.append(station.name, station.relative_water_level())

    expected_stations_highest_rel_level_sorted = \
        sorted(expected_stations_highest_rel_level, key=lambda x: x[1], reverse=True)[:N]
    actual_stations_highest_rel_level = stations_highest_rel_level(test_stations, N)

    assert expected_stations_highest_rel_level_sorted == actual_stations_highest_rel_level
