import pytest
from ml_data_analysis import summarize_mass, find_furthest_pair, read_data


def test_read_data():
    # Assuming the test CSV has known contents
    data = read_data("meteorite_landings.csv")
    assert len(data) > 0


def test_summarize_mass(capfd):
    # Test that summarize_mass prints expected output
    data = [{'mass': '10'}, {'mass': '20'}, {'mass': '30'}]
    summarize_mass(data)
    out, err = capfd.readouterr()
    assert "Total Mass: 60.0, Average Mass: 20.0" in out


def test_find_furthest_pair(capfd):
    # Test that find_furthest_pair prints expected output
    data = [{'name': 'Site1', 'reclat': '0', 'reclong': '0'},
            {'name': 'Site2', 'reclat': '90', 'reclong': '0'}]
    find_furthest_pair(data)
    out, err = capfd.readouterr()
    assert "Distance: 10007.543398010284 km" in out
