import json


def main():
    with open('./Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)

    for data in ml_data['meteorite_landings']:
        print('%s %sg'%(data['name'], data['mass (g)']))

if __name__ == '__main__':
    main()