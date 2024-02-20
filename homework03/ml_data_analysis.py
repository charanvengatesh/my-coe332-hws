import csv
import logging
from typing import List, Dict, Union
from gcd_algorithm import great_circle_distance

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_csv(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Reads CSV data into a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[Dict[str, Union[str, float]]]: A list of dictionaries representing the CSV rows.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []


def summarize_mass(records: List[Dict[str, str]]) -> None:
    """
    Calculates and prints summary statistics for meteorite masses.

    Args:
        records (List[Dict[str, str]]): List of meteorite landing records.
    """
    masses = [float(record['mass (g)'])
              for record in records if record['mass (g)']]
    if not masses:
        logging.warning("No mass data available.")
        return
    min_mass = min(masses)
    max_mass = max(masses)
    avg_mass = sum(masses) / len(masses)
    print(f"Mass Summary: Min = {min_mass}g, Max = {max_mass}g, Average = {avg_mass:.2f}g")


def calculate_distances(records: List[Dict[str, str]], sample_rate: int = 1) -> None:
    """
    Calculates and prints the distance between selected meteorite landing sites, based on a sampling rate.

    Args:
        records (List[Dict[str, str]]): List of meteorite landing records.
        sample_rate (int): The sampling rate for printing distances.

    """
    logging.info("Calculating distances between selected landing sites...")
    for i in range(0, len(records)-1, sample_rate):
        try:
            lat1, lon1 = float(records[i]['reclat']), float(
                records[i]['reclong'])
            lat2, lon2 = float(records[i+1]['reclat']
                               ), float(records[i+1]['reclong'])
            distance = great_circle_distance(lat1, lon1, lat2, lon2)
            # Log the distance for every 'sample_rate' pair of records
            print(f"Distance between {records[i]['name']} and {     records[i+1]['name']}: {distance:.2f} kilometers")
        except ValueError as e:
            logging.debug(f"Skipping calculation due to invalid data: {e}") 



if __name__ == "__main__":
    file_path = '../data/meteorite_landings.csv'
    data = read_csv(file_path)
    summarize_mass(data)
    # Prints every 4000th data point as the default value
    calculate_distances(data, sample_rate=4000)
