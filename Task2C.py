# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update water level
    update_water_levels(stations)

    # 10 Stations at which the current relative water level is highest
    print(stations_highest_rel_level(stations, 10))


if __name__ == "__main__":
    print("*** Task 2c: CUED Part IA Flood Warning System ***")
    run()
