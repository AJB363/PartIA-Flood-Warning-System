# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from floodsystem.utils import sorted_by_key # noqa


def stations_by_distance(stations, p):
    """ Returns the stations in order from closest to furthest from coordinate p """
    sorted_stations = []
    for station in stations:
        sorted_stations.append((station, haversine(station.coord, p)))
    sorted_stations = sorted_by_key(sorted_stations, 1)

    return sorted_stations


def stations_within_radius(stations, centre, r):
    """ Returns station within a radius r from the coordinate centre """
    within_radius = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            within_radius.append(station)
    return within_radius


def rivers_with_station(stations):
    """ Returns the set of rivers that have stations """
    rivers = set([])
    for station in stations:
        rivers.add(station.river)
    return rivers


def stations_by_river(stations):
    """ Returns a dictionary of stations, by the river they are next to """
    by_river = dict()
    for station in stations:
        if station.river not in by_river:
            by_river[station.river] = []
        by_river[station.river].append(station)
    return by_river


def rivers_by_station_number(stations, N):
    """ Returns a list of the N river names, and the count of how many stations are on the river,
    from largest count to smallest """
    # Get a dictionary of river names to counts
    river_station_count = dict()
    for station in stations:
        if station.river not in river_station_count:
            river_station_count[station.river] = 0
        river_station_count[station.river] += 1

    # Convert to a sorted list
    as_sorted_list = sorted([(key, river_station_count[key]) for key in river_station_count],
                            key=lambda x: x[1],
                            reverse=True)

    # Keep only the top N items
    top_N_rivers_by_count = []
    for i in range(N):
        j = 0
        while as_sorted_list[i][1] == as_sorted_list[i + j][1]:
            top_N_rivers_by_count.append(as_sorted_list[i + j])
            j += 1
    return top_N_rivers_by_count
