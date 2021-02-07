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
