"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
from haversine import haversine


def test_stations_by_distance_returns_given_stations_in_order_of_distance_from_a_coordinate_p():
    stations = []
    coords = [(-10.0, 0.0), (5.0, 5.0), (9.9, 9.9), (0.0, 0.0)]
    for i in range(len(coords)):
        # Create stations
        s_id = "test-s-id-" + str(i)
        m_id = "test-m-id-" + str(i)
        label = "some station " + str(i)
        coord = coords[i]
        trange = (-2.3, 3.4445)
        river = "River " + str(i)
        town = "My Town " + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    p = (10.0, 10.0)
    actual_sorted_stations = stations_by_distance(stations, p)
    expected_sorted_stations = [(stations[2], haversine(p, stations[2].coord)),
                                (stations[1], haversine(p, stations[1].coord)),
                                (stations[3], haversine(p, stations[3].coord)),
                                (stations[0], haversine(p, stations[0].coord))]

    assert expected_sorted_stations == actual_sorted_stations


def test_stations_within_radius_returns_all_stations_within_given_radius():
    stations = []
    coords = [(-10.0, 0.0), (5.0, 5.0), (9.9, 9.9), (0.0, 0.0)]
    for i in range(len(coords)):
        # Create stations
        s_id = "test-s-id-" + str(i)
        m_id = "test-m-id-" + str(i)
        label = "some station " + str(i)
        coord = coords[i]
        trange = (-2.3, 3.4445)
        river = "River " + str(i)
        town = "My Town " + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    centre = (10.0, 10.0)
    actual_stations = stations_within_radius(stations, centre, 1000.0)
    expected_stations = [stations[1], stations[2]]

    assert expected_stations == actual_stations
