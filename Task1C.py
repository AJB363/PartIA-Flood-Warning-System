from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""
    # Build list of stations
    stations = build_station_list()

    # Sort the stations by distance from cambridge centre
    centre = (52.2053, 0.1218)
    radius = 10.0
    within_radius = stations_within_radius(stations, centre, radius)

    # Print the stations
    stations = []
    for station in within_radius:
        stations.append(station.name)

    print(sorted(stations))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
