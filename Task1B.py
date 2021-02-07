from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Sort the stations by distance from cambridge centre
    p = (52.2053, 0.1218)
    sorted_stations = stations_by_distance(stations, p)

    # Print the closest and furthest 10
    stations = []
    for station in sorted_stations:
        stations.append((station[0].name, station[0].town, station[1]))

    print(stations[:10])
    print(stations[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
