from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()

    # Sort the stations by distance from cambridge centre
    rivers = rivers_with_station(stations)

    # Print the first 10 rivers
    print("{} stations. First 10 - {}".format(len(rivers), sorted(rivers)[:10]))

    # Get the dictionary of stations by river
    by_rivers = stations_by_river(stations)

    # Print the 3 entries
    print(sorted([station.name for station in by_rivers["River Aire"]]))
    print(sorted([station.name for station in by_rivers["River Cam"]]))
    print(sorted([station.name for station in by_rivers["River Thames"]]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
