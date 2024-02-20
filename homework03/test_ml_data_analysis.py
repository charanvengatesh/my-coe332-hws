from gcd_algorithm import great_circle_distance
from ml_data_analysis import read_csv, summarize_mass, calculate_distances


def test_read_csv():
    data = read_csv('../data/meteorite_landings.csv')
    assert len(data) > 0, "Data should not be empty"


def test_summarize_mass(capfd):
    data = [{'mass (g)': '10'}, {'mass (g)': '20'}, {'mass (g)': '30'}]
    summarize_mass(data)
    out, err = capfd.readouterr()
    expected_output = "Mass Summary: Min = 10.0g, Max = 30.0g, Average = 20.00g"
    assert expected_output in out, "Output should contain the correct mass summary"


def test_calculate_distances(capfd):
    data = [
        {'name': 'Site1', 'reclat': '0', 'reclong': '0'},
        {'name': 'Site2', 'reclat': '0', 'reclong': '180'}
    ]
    calculate_distances(data)
    out, err = capfd.readouterr()

    # Format the expected string to match the logging format in calculate_distances function
    expected_distance_km = great_circle_distance(0, 0, 0, 180)
    expected_distance_str = f"Distance between Site1 and Site2: {expected_distance_km:.2f} kilometers"
    assert expected_distance_str in out, f"Output should contain the correct distance calculation: {expected_distance_str}"

