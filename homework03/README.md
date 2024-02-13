# Meteorite Landings Analysis

### Overview

This repository contains scripts for analyzing meteorite landing data. The objective is to parse the data from a CSV file, calculate summary statistics, find the furthest pair of landing sites, and provide insights into the distribution of meteorite landings. This project serves as an educational tool for understanding data parsing, calculation of geographical distances, and basic data analysis principles.

### Contents

- `ml_data_analysis.py`: The primary script that reads the CSV data, calculates summary statistics, and finds the furthest pair of meteorite landing sites.
- `gcd_algorithm.py`: A secondary script that contains the great-circle distance function, used by the primary script to calculate distances between meteorite landing sites.
- `test_ml_data_analysis.py`: Contains unit tests for `ml_data_analysis.py` to ensure the correctness of its functionality.
- `test_gcd_algorithm.py`: Contains unit tests for the great-circle distance function in `gcd_algorithm.py`, ensuring accurate distance calculations.
- `README.md`: Provides an overview of the project, instructions for setting up and running the scripts, and guidelines for interpreting the results.



### Data Acquisition

To analyze meteorite landings, you will need the Meteorite Landings dataset available from NASA's open data portal. After downloading, place the CSV file in the same directory as the scripts.

### Running the Code

1. Ensure Python 3 and `pytest` are installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the `homework02` directory.
4. To run the primary analysis script, execute:

```
python meteorite_landings.py
```

5. To run the unit tests, ensure you are still in the `homework02` directory and execute:

```
pytest
```


### Interpreting Results

- The output of `meteorite_landings.py` will include the total and average mass of meteorites, as well as the furthest distance between two landing sites.
- The unit tests validate the accuracy of distance calculations and the correctness of the data parsing and summary statistics functions. Passing tests indicate that the scripts are functioning as expected.

### Conclusion

This project provides a hands-on approach to working with geographical data and performing basic analysis on meteorite landings. Through the use of Python scripts and unit testing, it offers insights into both software development and data analysis methodologies.
