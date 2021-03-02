from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import towns_most_at_risk


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
