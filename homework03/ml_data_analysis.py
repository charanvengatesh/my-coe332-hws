import csv
import logging
from typing import *
from gcd_algorithm import great_circle_distance

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Read meteorite landings data from a CSV file.

    Parameters:
    - file_path: Path to the CSV file.

    Returns:
    - A list of dictionaries, each representing a row from the CSV.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            logging.debug(f"Data successfully read from {file_path}")
            return data
    except Exception as e:
        logging.error(f"Failed to read data from {file_path}: {e}")
        return []


def summarize_mass(data: List[Dict[str, Any]]) -> None:
    """
    Print summary statistics for meteorite masses.

    Parameters:
    - data: List of meteorite landing data.
    """
    masses = [float(row['mass']) for row in data if row.get('mass')]
    total_mass = sum(masses)
    average_mass = total_mass / len(masses) if masses else 0
    logging.debug(f"Total mass: {total_mass}, Average mass: {average_mass}")
    print(f"Total Mass: {total_mass}, Average Mass: {average_mass}")


def find_furthest_pair(data: List[Dict[str, Any]]) -> None:
    """
    Find and print the furthest pair of meteorite landing sites.

    Parameters:
    - data: List of meteorite landing data.
    """
    max_distance = 0
    furthest_pair = (None, None)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            lat1, lon1 = float(data[i]['reclat']), float(data[i]['reclong'])
            lat2, lon2 = float(data[j]['reclat']), float(data[j]['reclong'])
            distance = great_circle_distance(lat1, lon1, lat2, lon2)
            if distance > max_distance:
                max_distance = distance
                furthest_pair = (data[i]['name'], data[j]['name'])
    logging.debug(f"Furthest pair: {
                  furthest_pair} with distance: {max_distance} km")
    print(f"Furthest Pair: {furthest_pair}, Distance: {max_distance} km")


# Example usage
if __name__ == "__main__":
    data = read_data("meteorite_landings.csv")
    summarize_mass(data)
    find_furthest_pair(data)
