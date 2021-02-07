"""Unit test for the geo module"""

import floodsystem.geo as geo
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
    actual_sorted_stations = geo.stations_by_distance(stations, p)
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
    actual_stations = geo.stations_within_radius(stations, centre, 1000.0)
    expected_stations = [stations[1], stations[2]]

    assert expected_stations == actual_stations


def test_rivers_with_station_returns_all_rivers():
    stations = []
    rivers = ["A", "B", "C", "A", "B", "D", "E"]
    for i in range(len(rivers)):
        # Create stations
        s_id = "test-s-id-" + str(i)
        m_id = "test-m-id-" + str(i)
        label = "some station " + str(i)
        coord = (0.0, 0.0)
        trange = (-2.3, 3.4445)
        river = rivers[i]
        town = "My Town " + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    actual_rivers = geo.rivers_with_station(stations)
    expected_rivers = {"A", "B", "C", "D", "E"}

    assert actual_rivers == expected_rivers


def test_stations_by_river_returns_a_dictionary_of_stations_by_rivers():
    stations = []
    rivers = ["A", "B", "C", "A", "B", "D", "E"]
    for i in range(len(rivers)):
        # Create stations
        s_id = "test-s-id-" + str(i)
        m_id = "test-m-id-" + str(i)
        label = "some station " + str(i)
        coord = (0.0, 0.0)
        trange = (-2.3, 3.4445)
        river = rivers[i]
        town = "My Town " + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    actual_stations_by_rivers = geo.stations_by_river(stations)
    expected_stations_by_rivers = dict()
    expected_stations_by_rivers["A"] = [stations[0], stations[3]]
    expected_stations_by_rivers["B"] = [stations[1], stations[4]]
    expected_stations_by_rivers["C"] = [stations[2]]
    expected_stations_by_rivers["D"] = [stations[5]]
    expected_stations_by_rivers["E"] = [stations[6]]

    assert actual_stations_by_rivers == expected_stations_by_rivers


def test_rivers_by_station_number_returns_a_list_of_river_names_with_the_number_of_stations_in_each():
    stations = []
    rivers = ["A", "B", "C", "A", "B", "D", "E", "B", "A", "C", "B", "D"]
    for i in range(len(rivers)):
        # Create stations
        s_id = "test-s-id-" + str(i)
        m_id = "test-m-id-" + str(i)
        label = "some station " + str(i)
        coord = (0.0, 0.0)
        trange = (-2.3, 3.4445)
        river = rivers[i]
        town = "My Town " + str(i)
        stations.append(MonitoringStation(s_id, m_id, label, coord, trange, river, town))

    actual_rivers_by_station_number = geo.rivers_by_station_number(stations, 3)
    expected_rivers_by_station_number = [("B", 4), ("A", 3), ("C", 2), ("D", 2)]

    print(actual_rivers_by_station_number)

    assert actual_rivers_by_station_number == expected_rivers_by_station_number
