import yaml

data = {}

def main():
    with open('./Meteorite_Landings.yaml', 'r') as f:
        ml_data = yaml.load(f, Loader=yaml.SafeLoader)

    for data in ml_data['meteorite_landings']:
        print('%s %sg' % (data['name'], data['mass (g)']))


if __name__ == '__main__':
    main()
