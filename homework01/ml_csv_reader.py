import csv


ml_data = {}
ml_data['meteorite_landings'] = []

def main():
    with open('./Meteorite_Landings.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ml_data['meteorite_landings'].append(dict(row))
        for data in ml_data['meteorite_landings']:
            print('%s %sg' % (data['name'], data['mass (g)']))


if __name__ == '__main__':
    main()
